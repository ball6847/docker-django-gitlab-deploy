DJANGO GIT DEPLOY
=================

Simple git webhook endpoint for Gogs written in Django

## INSTALLATION

```shell
# grab a copy from git
git clone git@gitlab.bizidea.co.th:bizidea-tools/django-gitlab-deploy.git
cd django-gitlab-deploy

# install and activate virtualenv
virtualenv .venv
source .venv/bin/activate

# install dependencies using pip
pip install -r requirements.txt

# install databases, you will be asked to create a superadmin account
python manage.py syncdb
python manage.py migrate

# collect all static files from package to /static/ directory (you might want to setup nginx to serve these files)
python manage.py collectstatic

# to run a development server
python manage.py runserver 0.0.0.0:8000

```

To run a production server using gunicorn use the following command

```shell
gunicorn --workers=2 wsgi
```

Note
- You might to use process manager like supervisord to create a daemon for the app
- gunicorn won't serve static files, you need to setup webserver like nginx by yourself
- You need to run application as root if you want to let the application manage ownershop of the created files
