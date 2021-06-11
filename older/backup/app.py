# -*- coding:utf-8 -*-
from flask import *
import settings
from read_doc import *

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def home():
    release = info(filename="doc/release.xlsx", sheetname="plan", max_line=8)
    infox = basic("doc/release.xlsx", "links")
    dct = make_dct(infox)
    w = (100 - 10) / (len(dct) + 2)
    return render_template("home.html", release=release, dd=dct, wd=w)


@app.route('/CAM')
def CAM():
    return render_template("CAM.html")


@app.route('/BCA')
def BCA():
    BC_info = info(filename="doc/release.xlsx", sheetname="BCA")

    return render_template("BCA.html", BC_info=BC_info)


@app.route('/deploy')
def deploy():
    return render_template("deploy.html")


@app.route('/SQL')
def SQL():
    return render_template("SQL.html")


if __name__ == "__main__":
    app.run()
