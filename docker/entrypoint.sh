#!/bin/sh

cd /app

CONFIGFILE="settings/environment/config.py"

if [[ ! -f "settings/environment/__init__.py" ]]; then
  touch settings/environment/__init__.py
fi

# ----------------------------------------------------------------
# create config file if neccessary

if [[ ! -f "$CONFIGFILE" ]]; then
  SECRET_KEY=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
  echo "
import os

SECRET_KEY = '$SECRET_KEY'
SSH_PRIVATE_KEY = os.path.join(os.path.dirname(__file__), 'id_rsa')
SSH_PUBLIC_KEY = os.path.join(os.path.dirname(__file__), 'id_rsa.pub')
SSH_KEY_PASSPHRASE = ''

" > $CONFIGFILE
fi

# ----------------------------------------------------------------

python manage.py migrate
python manage.py collectstatic --noinput

# TODO: user environment variables for superadmin
echo "
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admim@domain.com', 'changethis987654321')
" | python manage.py shell > /dev/null 2>&1

DJANGO_SETTINGS_MODULE="settings.base" celery -A tasks worker --loglevel=info --concurrency=1&

# TODO: use gunicorn + nginx in production
python manage.py runserver 0.0.0.0:8000
