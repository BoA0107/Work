# -*- coding:utf-8 -*-
from flask import *
import settings
from read_doc import read_doc

app1 = Flask(__name__)
app1.config.from_object(settings)


@app1.route('/')
def show():
    xx = read_doc(filename='doc/release.xlsx', sheetname='plan', mode=1, max_line=8)
    return render_template("show.html", x=xx)


if __name__ == "__main__":
    app1.run()
