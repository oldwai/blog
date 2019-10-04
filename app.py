"""
------------------------------
#project_name: py.github.io
#create_time：2019/10/4 17:24
#author：Administrator

------------------------------
"""

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello everyBody'