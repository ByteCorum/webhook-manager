#!/bin/bash

python3 -m nuitka \
    --follow-imports \
    --remove-output \
    --assume-yes-for-downloads \
    --onefile \
    --output-filename=webhook-controller \
    --linux-icon=assets/program/icon.png \
    --enable-plugin=tk-inter \
    --company-name="ByteCorum" \
    --product-name="webhook-controller" \
    --file-version=1.0.0.5 \
    --product-version=1.0.0.5 \
    --file-description="Python GUI cross-platform prigram for controlling discord webhooks" \
    --copyright="https://github.com/ByteCorum/WebhookController/blob/main/LICENSE" \
    src/main.py
