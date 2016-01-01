#!/bin/sh

echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
apk update
apk add python py-pip libgit2@testing
pip install cffi 
