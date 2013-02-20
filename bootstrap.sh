#!/usr/bin/env ash
rm -rf venv
virtualenv --system-site-packages venv
source venv/bin/activate
pip install tornado tornadio2 sockjs-tornado
echo Activate with source venv/bin/activate
