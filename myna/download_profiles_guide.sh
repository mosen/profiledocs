#!/bin/bash

if [[ ! -f ./Configuration-Profile-Reference.pdf ]]; then
    echo "No configuration profile reference found, downloading..."
    curl -O https://developer.apple.com/enterprise/documentation/Configuration-Profile-Reference.pdf
fi


if [[ ! -f ./MDM-Protocol-Reference.pdf ]]; then
    echo "No MDM protocol reference found, downloading..."
    curl -O https://developer.apple.com/enterprise/documentation/MDM-Protocol-Reference.pdf
fi


echo "Done!"
