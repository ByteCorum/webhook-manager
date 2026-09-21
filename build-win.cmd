@echo off

python.exe -m nuitka ^
    --follow-imports ^
    --remove-output ^
    --assume-yes-for-downloads ^
    --onefile ^
    --output-filename=webhook-controller ^
    --windows-icon-from-ico=assets/program/icon.ico ^
    --enable-plugin=tk-inter ^
    --company-name="ByteCorum" ^
    --product-name="webhook-controller" ^
    --file-version=1.0.0.5 ^
    --product-version=1.0.0.5 ^
    --file-description="Python GUI cross-platform prigram for controlling discord webhooks" ^
    --copyright="https://github.com/ByteCorum/WebhookController/blob/main/LICENSE" ^
    src/main.py
