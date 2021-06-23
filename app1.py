# -*- coding:utf-8 -*-

from flask import *
from readdoc import *

app = Flask(__name__)

filename = r"doc/info.xlsx"
sheet_deploy = r"deploy_plan"
sheet_links = r"links"
sheet_career = r"level_info"
sheet_SQL = r"SQL"
sheet_BCA_data = r"BCA_data"


#SQL
filename_SQL = r"doc/SQL.xlsx"
sheet_SQL_batch = r'batch_SQL'




@app.route('/')
def show():
    return render_template('show.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    # plan_info
    plan_info = read_doc(filename=filename, sheetname=sheet_deploy, max_line=16)

    # links
    links = read_doc(filename=filename, sheetname=sheet_links)
    links_dct = make_dct(links)

    # career_level
    career_level = read_doc(filename=filename, sheetname=sheet_career)

    return render_template("home.html", plan_info=plan_info, links=links_dct, career_level=career_level)


@app.route('/SQL')
def SQL():
    batch_data= read_doc(filename=filename_SQL,sheetname=sheet_SQL_batch)

    return render_template('SQL.html', batch_data=batch_data)


@app.route('/deploy')
def deploy():
    return render_template('deploy.html')


@app.route('/项目_01')
def project_01():
    return render_template('项目_01.html')


@app.route('/BCA')
def BCA():
    BCA_data = read_doc(filename=filename, sheetname=sheet_BCA_data)
    return render_template('BCA.html', BCA_data=BCA_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=666, debug=True)
