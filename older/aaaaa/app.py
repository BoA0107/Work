# -*- coding:utf-8 -*-

from flask import *
from read import *

app = Flask(__name__)

filename = r"doc/release.xlsx"
sheet_release_plan = r"Release_Plan"
sheet_links = r"links"
sheet_Level_Info = r"Level_Info"
sheet_BCA = r"BCA"


@app.route('/')
def show():
    return render_template('show.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    release = read_doc(filename=filename, sheetname=sheet_release_plan, max_line=8)
    links = read_doc(filename=filename, sheetname=sheet_links)
    links_dct = make_dct(links)
    level_info = read_doc(filename=filename, sheetname=sheet_Level_Info)
    return render_template('home.html', release=release, links=links_dct,level_info=level_info)


@app.route('/BCA')
def BCA():
    return render_template('BCA.html')


@app.route('/deploy')
def deploy():
    return render_template('deploy.html')


@app.route('/CAM')
def CAM():
    return render_template('CAM.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
