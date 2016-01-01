#!/bin/sh

cd /app

python manage.py syncdb --noinput
python manage.py migrate
python manage.py collectstatic --noinput

# TODO: user environment variables for superadmin
echo "
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admim@domain.com', 'changethis987654321')
" | python manage.py shell > /dev/null 2>&1

celery -A tasks worker --loglevel=info&

# TODO: use gunicorn + nginx in production
python manage.py runserver 0.0.0.0:8000
