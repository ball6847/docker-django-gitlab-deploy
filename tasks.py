from celery import Celery
from unipath import Path
import pygit2 as git
import os
from apps.project.utils import get_closest_uid

# setup Celery
app = Celery('tasks', backend='amqp', broker='amqp://guest:guest@rabbitmq:5672//')
app.conf.CELERY_TASK_SERIALIZER = 'json'
app.conf.CELERY_ACCEPT_CONTENT = ['json']

ssh_user = "git"
private_key = "id_rsa"
public_key = "id_rsa.pub"

@app.task(ignore_result=True)
def deploy(project):
    print("Starting project deployment")

    # ssh credentials
    credential = git.Keypair("git", public_key, private_key, "")
    git.settings.search_path[git.GIT_CONFIG_LEVEL_GLOBAL] = '/var/lib/nobody'
    callback = git.RemoteCallbacks(credential)

    path = Path(project['path'])
    uid = get_closest_uid(path)
    pid = os.fork()

    if pid == 0:
        try:
            if uid != 0:
                os.setgid(uid)
                os.setuid(uid)

            # git dir suppose to be a directory not a file
            if path.isfile():
                print("Expected deploy path to be a directory")
                return

            if not path.isdir():
                repo = git.clone_repository(project['repo'], path, bare=False, callbacks=callback)
                print("Cloned %s into %s" % (project['repo'], path))
            else:
                repo = git.Repository(os.path.join(path, '.git'))
                # fetch from remote
                remote = repo.remotes[0]
                remote.fetch(callbacks=callback)
                # reset all local change
                head = repo.revparse_single("FETCH_HEAD")
                repo.reset(head.id, git.GIT_RESET_HARD)
                print("Updated %s" % (project['repo']))
        except Exception as e:
            print(e)
            view_traceback()
        finally:
            os._exit(0)

    os.waitpid(pid, 0)
    print("Done.")

def view_traceback():
    ex_type, ex, tb = sys.exc_info()
    traceback.print_tb(tb)
    del tb
