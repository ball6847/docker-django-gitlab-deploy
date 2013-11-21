DEBUG = False
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'Asia/Bangkok'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': '',                      # Or path to database file if using sqlite3.
		# The following settings are not used with sqlite3:
		'USER': '',
		'PASSWORD': '',
		'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
		'PORT': '',                      # Set to empty string for default.
	}
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ktluyf=j=chx8+%dz*1c^8j%^ru3u5fs6-+z+07w+nz_&y5e!-'