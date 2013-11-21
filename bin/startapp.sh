#! /usr/bin/env bash

cd "$(dirname $0)/.."

if [[ -d "apps/$1" ]]; then
	echo "apps/$1 already exists"
	exit 1
fi

mkdir "apps/$1"
python manage.py startapp "$1" "apps/$1"