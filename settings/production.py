from .base import PROJECT_ROOT

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'Asia/Bangkok'

# you need to change this on production environment
ALLOWED_HOSTS = []

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': PROJECT_ROOT.child('db', 'database.sqlite'),                      # Or path to database file if using sqlite3.
	}
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ktluyf=j=chx8+%dz*1c^8j%^ru3u5fs6-+z+07w+nz_&y5e!-'
