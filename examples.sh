#!/usr/bin/env bash
DESTDIR="./source/_static/examples"

for filename in ./source/_static/manifests/*.plist; do
    echo ${filename}
    BASENAME=$(basename "${filename}")

    python ./pfm2template/pfm2template.py -o "${DESTDIR}" "${filename}"
done