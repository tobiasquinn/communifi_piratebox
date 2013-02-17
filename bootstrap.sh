#!/usr/bin/env ash
rm -rf venv
virtualenv --system-site-packages venv
source venv/bin/activate
pip install tornado
echo Activate with source venv/bin/activate
