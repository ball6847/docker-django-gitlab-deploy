#! /usr/bin/env bash

git clean -fdx
git fetch -f origin master
git reset --hard FETCH_HEAD