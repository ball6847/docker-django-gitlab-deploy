from .base import PROJECT_ROOT, ADMINS

# change to True in development
DEBUG = False
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'Asia/Bangkok'

ADMIN += (
    ('ball6847', 'porawit.p@bizidea.co.th'),
)

# you need to change this on production environment
ALLOWED_HOSTS = ['.gitlab-deploy.bizidea.co.th']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': PROJECT_ROOT.child('db', 'database.sqlite'),                      # Or path to database file if using sqlite3.
	}
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ktluyf=j=chx8+%dz*1c^8j%^ru3u5fs6-+z+07w+nz_&y5e!-'

# email setting, need if you need django to send email to ADMIN when errors occured
EMAIL_HOST = '127.0.0.1'
EMAIL_HOST_USER = 'bizidea'
EMAIL_HOST_PASSWORD = 'nyGJELRR'
EMAIL_PORT = 25
EMAIL_USE_TLS = False