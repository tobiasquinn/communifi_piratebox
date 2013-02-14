#!/usr/bin/env python
from flask import Flask, render_template, send_file
app = Flask(__name__)

@app.route('/', defaults={'path': '/index.html'})
@app.route('/<path:path>')
def catch_all(path):
    return send_file('app/%s' % (path))

if __name__ == '__main__':
    app.debug = True
    print app.url_map
    app.run(host='0.0.0.0', port=6001)
