#!/usr/bin/env ash
rm -rf venv
virtualenv --system-site-packages venv
source venv/bin/activate
pip install flask cherrypy
#pip install flask-sass frozen-flask flask-markdown
echo Activate with source venv/bin/activate
