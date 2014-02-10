#! /usr/bin/env bash

# used in production server only

PSCOUNT="$(ps aux | grep [g]itlab_deploy_server | wc -l)"

if [ "$PSCOUNT" -eq "0" ]; then
    cd "$(dirname $0)/.."
    source .virtualenv/bin/activate
    gunicorn wsgi:application --name gitlab_deploy_server --workers 3 --bind=unix:/var/run/gitlab_deploy_server.sock --daemon
fi

