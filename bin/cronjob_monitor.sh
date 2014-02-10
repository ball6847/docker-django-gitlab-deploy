#! /usr/bin/env bash

# used in production server only

PSCOUNT="$(ps aux | grep [g]itlab_deployd | wc -l)"

if [ "$PSCOUNT" -eq "0" ]; then
    echo "$(date +"%D %T")" " - starting gitlab_deploy_server"
    cd "$(dirname $0)/.."
    source .virtualenv/bin/activate
    gunicorn wsgi:application --name gitlab_deployd --workers 3 --bind=unix:/var/run/gitlab_deploy_server.sock --daemon
fi

