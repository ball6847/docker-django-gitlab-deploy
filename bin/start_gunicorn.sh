#!/bin/bash

cd "$(dirname $0)/.."

NAME="gitlab_deploy_server"
BIND=127.0.0.1:54321
NUM_WORKERS=1
DJANGO_SETTINGS_MODULE="settings.base"
DJANGO_WSGI_MODULE="wsgi"

if [[ $VIRTUAL_ENV = "" ]]; then
	VIRTUAL_ENV=".venv"
	source "$VIRTUAL_ENV/bin/activate"
fi

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$PWD:$PYTHONPATH

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec "$VIRTUAL_ENV/bin/gunicorn" "$DJANGO_WSGI_MODULE:application" \
	--name $NAME \
	--workers $NUM_WORKERS \
	--log-level=debug \
	--bind=$BIND
