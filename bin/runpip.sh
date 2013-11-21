#!/usr/bin/env bash

PYIP_DOWNLOAD_CACHE="$HOME/.pyip"

cd "$(dirname $0)/.."

while read package
do
    if [[ "$package" != "" ]]; then
        pip install --download-cache $PYIP_DOWNLOAD_CACHE $package
    fi
done < requirements.txt