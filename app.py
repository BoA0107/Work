# -*- coding:utf-8 -*-

from flask import *

app = Flask(__name__)


@app.route('/')
def show():
    return render_template('show.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/SQL')
def SQL():
    return render_template('SQL.html')


@app.route('/deploy')
def deploy():
    return render_template('deploy.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=666, debug=True)
