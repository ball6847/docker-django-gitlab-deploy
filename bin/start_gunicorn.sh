#!/bin/bash

cd "$(dirname $0)/.."

NAME="gitlab_deploy_server"
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE="settings.base"
DJANGO_WSGI_MODULE="wsgi"

if [[ $VIRTUAL_ENV = "" ]]; then
	VIRTUAL_ENV=".virtualenv"
	source "$VIRTUAL_ENV/bin/activate"
fi

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$PWD:$PYTHONPATH

SOCKFILE="/var/run/gitlab_deploy_server.sock"

# Create the run directory if it doesn't exist
RUNDIR="$(dirname $SOCKFILE)"
test -d $RUNDIR || mkdir -p $RUNDIR

echo "starting gunicorn using unix socket: $SOCKFILE"
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec "$VIRTUAL_ENV/bin/gunicorn" "$DJANGO_WSGI_MODULE:application" \
	--name $NAME \
	--workers $NUM_WORKERS \
	--log-level=debug \
	--bind=unix:$SOCKFILE