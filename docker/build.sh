#!/bin/sh

cd /app

echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
apk add --update gcc libffi-dev musl-dev python-dev py-pip libgit2-dev@testing==0.23.2

# pygit2 need cffi at compile time, so we need to install it first
pip install cffi
pip install -r requirements.txt
