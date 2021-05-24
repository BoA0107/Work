# -*- coding:utf-8 -*-

from flask import *
from read import *

app = Flask(__name__)

filename = r"doc/release.xlsx"
sheet_BCA = "BCA"
sheet_plan = "plan"

@app.route('/table')
def talbe():
    plan_info=read_doc(filename=filename,sheetname=sheet_plan,max_line=8)
    return render_template("table.html", plan_info=plan_info)


if __name__ == "__main__":
    app.run(debug=True)
