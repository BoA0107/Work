# -*- coding:utf-8 -*-

from flask import *

app = Flask(__name__)


@app.route('/')
def show():
    return ('hello world')


if __name__ == '__main__':
    app.run(debug=True)
