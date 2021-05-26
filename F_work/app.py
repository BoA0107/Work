# -*- coding:utf-8 -*-

from flask import *
from read import *

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


app.run(debug=True)
