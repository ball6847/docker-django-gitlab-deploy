from celery import Celery
from unipath import Path
import pygit2 as git
from settings.base import SSH_PRIVATE_KEY, SSH_PUBLIC_KEY, SSH_KEY_PASSPHRASE
import os
from apps.project.utils import get_closest_uid, shell_exec

# setup Celery
app = Celery('tasks',
    broker='amqp://guest:guest@rabbitmq:5672//',
    backend='amqp'
)
app.conf.CELERY_TASK_SERIALIZER = 'json'
app.conf.CELERY_ACCEPT_CONTENT = ['json']

@app.task(ignore_result=True)
def deploy(project):
    print("Starting project deployment")

    # ssh credentials
    credential = git.Keypair("git", SSH_PUBLIC_KEY, SSH_PRIVATE_KEY, SSH_KEY_PASSPHRASE)
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

    compose = Path(path, 'docker-compose.yml')

    if compose.isfile():
        print(shell_exec(['docker-compose', '-f', compose, 'up', '-d']))

    print("Done.")

def view_traceback():
    ex_type, ex, tb = sys.exc_info()
    traceback.print_tb(tb)
    del tb
