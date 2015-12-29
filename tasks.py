from celery import Celery
from unipath import Path
from pygit2 import Keypair, Repository, GIT_RESET_HARD, clone_repository
import os
from apps.project.utils import get_closest_uid

# setup Celery
app = Celery('tasks', backend='amqp', broker='amqp://')
app.conf.CELERY_TASK_SERIALIZER = 'json'
app.conf.CELERY_ACCEPT_CONTENT = ['json']

ssh_user = "git"
private_key = "id_rsa"
public_key = "id_rsa.pub"

@app.task(ignore_result=True)
def deploy(project):
    print("Starting project deployment")

    # ssh credentials
    cred = Keypair("git", public_key, private_key, "")
    path = Path(project['path'])
    uid = get_closest_uid(path)
    pid = os.fork()

    if pid == 0:
        try:
            os.setgid(uid)
            os.setuid(uid)

            # git dir suppose to be a directory not a file
            if path.isfile():
                print("Expected deploy path to be a directory")
                return

            if not path.isdir():
                repo = clone_repository(project['repo'], path, bare=False, credentials=cred)
                print("Cloned %s into %s" % (project['repo'], path))
            else:
                repo = Repository(os.path.join(path, '.git'))
                # fetch from remote
                remote = repo.remotes[0]
                remote.credentials = cred
                remote.fetch()
                # reset all local change
                head = repo.revparse_single("HEAD")
                repo.reset(head.id, GIT_RESET_HARD)
                print("Updated %s" % (project['repo']))
        except Exception as e:
            print(e)
        finally:
            os._exit(0)

    os.waitpid(pid, 0)
    print("Done.")
