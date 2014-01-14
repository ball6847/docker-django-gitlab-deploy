#! /usr/bin/env sh
# chkconfig: 2345 55 45
# description: start or stop gunicorn

# chkconfig –add gunicorn in centos and redhat
# update-rc.d gunicorn defaults in debian and ubuntu

### BEGIN INIT INFO
# Provides:          gitlab_deploy_server
# Required-Start:    $all
# Required-Stop:     $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts the gunicorn server
# Description:       starts gunicorn using start-stop-daemon
### END INIT INFO

# Gunicorn init.d script for debian/ubuntu
# Written by Wojtek 'suda' Siudzinski <admin@suda.pl>
# Gist: https://gist.github.com/748450
#
# Sample config (/etc/default/gunicorn):
#
# SERVERS=(
#   'server_name    port    project_path    number_of_workers'
# )
# RUN_AS='www-data'
#
# WARNING: user $RUN_AS must have +w on /var/run/gunicorn

cd "$(dirname $0)/.."

NAME=gitlab_deploy_server
DESC=Gitlab Deploy Server
NUM_WORKERS=3
SOCKFILE="$PWD/var/run/gunicorn.sock"
PIDFILE="$PWD/var/run/gunicorn.pid"
DJANGO_SETTINGS_MODULE="settings.base"
DJANGO_WSGI_MODULE="wsgi:application"

if [[ $VIRTUAL_ENV = "" ]]; then
	VIRTUAL_ENV=".virtualenv"
fi

PATH=$VIRTUAL_ENV/bin:$PATH
PYTHONHOME=""
DAEMON=$VIRTUAL_ENV/bin/gunicorn

test -x $DAEMON || exit 0

start () {
    echo "Spawning $DESC"

    $DAEMON $DJANGO_WSGI_MODULE \
        --daemon \
        --name    $NAME \
        --workers $NUM_WORKERS \
        --bind    unix:$SOCKFILE \
        --pid     $PIDFILE

    return
}

stop () {
    if [ -f $PIDFILE ]; then
        echo "Killing $NAME"
        kill $(cat $PIDFILE)
    fi
}

case "$1" in
    start)
        echo "Starting $DESC"
        start
        ;;
    stop)
        echo "Stopping $DESC"
        stop
        ;;
    restart)
        echo "Restarting $DESC"
        stop
        sleep 1
        start
        ;;
    *)
        N=/etc/init.d/$NAME
        echo "Usage: $N {start|stop|restart} " >&2
        exit 1
        ;;
esac

exit 0