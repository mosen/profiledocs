#!/usr/bin/env bash
DESTDIR="./source/_static/json-schema"

for filename in ./source/_static/manifests/*.plist; do
    echo ${filename}
    BASENAME=$(basename "${filename}")

    python ./pfm2jsonschema/pfm2jsonschema.py -o "${DESTDIR}" "${filename}"
done

for filename in ./source/payloads/manifests/manual/*.plist; do
    echo ${filename}
    BASENAME=$(basename "${filename}")

    python ./pfm2jsonschema/pfm2jsonschema.py -o "${DESTDIR}" "${filename}"
done