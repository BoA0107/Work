# -*- coding:utf-8 -*-

from flask import *
from read import *

app = Flask(__name__)

filename = r"doc/release.xlsx"
sheet_BCA = "BCA"
sheet_plan = "plan"
sheet_links="links"


@app.route('/table')
def talbe():
    # 发布计划
    plan_info = read_doc(filename=filename, sheetname=sheet_plan, max_line=8)

    # BC
    BC_info =read_doc(filename=filename, sheetname=sheet_BCA)


#links
    links =read_doc(filename=filename, sheetname=sheet_BCA)
    return render_template("table.html", plan_info=plan_info,BC_info=BC_info,links=links)
if __name__ == "__main__":
    app.run(debug=True)
