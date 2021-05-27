# -*- coding:utf-8 -*-

from flask import *
from read import *

app = Flask(__name__)

filename = r"doc/release.xlsx"
sheet_BCA = "BCA"
sheet_plan = "plan"
sheet_links = "links"


@app.route('/base')
def base():
    return render_template('show.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/BCA')
def BCA():
    return render_template('BCA.html')


@app.route('/CAM')
def CAM():
    return render_template('CAM.html')


@app.route('/deploy')
def deploy():
    return render_template('deploy.html')


@app.route('/SQL')
def SQL():
    return render_template('SQL.html')


@app.route('/table')
def talbe():
    # 发布计划
    plan_info = read_doc(filename=filename, sheetname=sheet_plan, max_line=8)

    # BC
    BC_info = read_doc(filename=filename, sheetname=sheet_BCA)

    # links
    links = read_doc(filename=filename, sheetname=sheet_links)
    links_dct = make_dct(links)

    return render_template("table.html", plan_info=plan_info, BC_info=BC_info, links=links_dct)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
