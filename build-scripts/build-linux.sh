#!/bin/bash

python3 -m nuitka \
    --follow-imports \
    --remove-output \
    --assume-yes-for-downloads \
    --onefile \
    --output-filename="webhook-manager" \
    --linux-icon="../assets/program/icon.png" \
    --enable-plugin=tk-inter \
    --company-name="ByteCorum" \
    --product-name="webhook-manager" \
    --linux-app-license="GPL v3" \
    --file-version="1.0.0.5" \
    --product-version="1.0.0.5" \
    --file-description="Comprehensive control panel for managing and controlling all your Discord Webhooks seamlessly" \
    --copyright="https://github.com/ByteCorum/webhook-manager/blob/main/LICENSE" \
    ../src/main.py
