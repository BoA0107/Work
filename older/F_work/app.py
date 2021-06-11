# -*- coding:utf-8 -*-

from flask import *
from read import *
from SQL_Dct import *

filename = r"doc/release.xlsx"
sheet_BCA = "BCA"
sheet_plan = "plan"
sheet_links = "links"

app = Flask(__name__)


@app.route("/")
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
    return render_template("BCA.html", BC_info=BC_info)


@app.route('/SQL')
def SQL():
    SQLDCT = SQLD
    return render_template("SQL.html", SQLDCT=SQLDCT)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
