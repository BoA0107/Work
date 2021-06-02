# -*- coding:utf-8 -*-

from flask import *
from read import *
from SQL_Dct import *

filename = r"doc/release.xlsx"
sheet_BCA = "BCA"
sheet_plan = "plan"
sheet_links = "links"
sheet_Level_Info='Level_Info'

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('show.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    # 发布计划
    plan_info = read_doc(filename=filename, sheetname=sheet_plan, max_line=8)

    # links
    links = read_doc(filename=filename, sheetname=sheet_links)
    links_dct = make_dct(links)

    return render_template("home.html", plan_info=plan_info, links=links_dct)


@app.route('/BCA')
def BCA():
    # BC
    BC_info = read_doc(filename=filename, sheetname=sheet_BCA)
    SQLBCA = SQL_BCA
    return render_template("BCA.html", BC_info=BC_info,SQLBCA=SQLBCA)


@app.route('/SQL')
def SQL():
    SQLDCT = SQLD
    return render_template("SQL.html", SQLDCT=SQLDCT)


@app.route('/Deploy')
def Deploy():
    return render_template('Deploy.html')


@app.route('/table')
def table():
    Level_Info = read_doc(filename=filename, sheetname=sheet_Level_Info)
    return render_template('table.html',Level_Info=Level_Info)


if __name__ == '__main__':
    app.run(debug=True,port=5001)
