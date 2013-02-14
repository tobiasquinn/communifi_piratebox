#!/usr/bin/env bash
rm -rf venv
virtualenv venv
source venv/bin/activate
pip install flask
#pip install flask-sass frozen-flask flask-markdown
echo Activate with source venv/bin/activate
