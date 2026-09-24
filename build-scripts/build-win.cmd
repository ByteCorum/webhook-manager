@echo off

python.exe -m nuitka ^
    --follow-imports ^
    --remove-output ^
    --assume-yes-for-downloads ^
    --onefile ^
    --output-filename="webhook-manager" ^
    --windows-icon-from-ico="assets/program/icon.ico" ^
    --enable-plugin=tk-inter ^
    --company-name="ByteCorum" ^
    --product-name="webhook-manager" ^
    --file-version="1.0.0.5" ^
    --product-version="1.0.0.5" ^
    --file-description="Comprehensive control panel for managing and controlling all your Discord Webhooks seamlessly" ^
    --copyright="https://github.com/ByteCorum/webhook-manager/blob/main/LICENSE" ^
    src/main.py
