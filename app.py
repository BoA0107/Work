# -*- coding:utf-8 -*-

from flask import *
from readdoc import *

app = Flask(__name__)

filename = r"doc/info.xlsx"
sheet_deploy = r"deploy_plan"
sheet_links = r"links"
sheet_SQL = r"SQL"

plan_info = read_doc(filename=filename, sheetname=sheet_deploy, max_line=8)


@app.route('/')
def show():
    return render_template('show.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    #plan_info
    plan_info = read_doc(filename=filename, sheetname=sheet_deploy, max_line=8)

    # links
    links = read_doc(filename=filename, sheetname=sheet_links)
    links_dct = make_dct(links)

    return render_template("home.html", plan_info=plan_info, links=links_dct)


@app.route('/SQL')
def SQL():
    return render_template('SQL.html')


@app.route('/deploy')
def deploy():
    return render_template('deploy.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=666, debug=True)
