from .base import PROJECT_ROOT

# change to True in development
DEBUG = True

TIME_ZONE = 'Asia/Bangkok'

# you need to change this on production environment
ALLOWED_HOSTS = ['*']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'django',                      # Or path to database file if using sqlite3.
		# The following settings are not used with sqlite3:
		'USER': 'django',
		'PASSWORD': 'changethis123',
		'HOST': 'postgresql',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
		'PORT': '5432',                      # Set to empty string for default.
	}
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ktluyf=j=chx8+%dz*1c^8j%^ru3u5fs6-+z+07w+nz_&y5e!-'
