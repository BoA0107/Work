# -*- coding: UTF-8 -*-
from func.func_home import *
from func.func_BCA import *
from func.func_SQL import *
from func.func_deploy import *

app = Flask(__name__)


@app.route('/')
def show():
    return render_template('show.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template("home.html", plan_info=plan_info, links=links_dct, career_level=career_level, others=others)


@app.route('/BCA')
def BCA():
    return render_template('BCA.html', UAT_BC=UAT_BC)


@app.route('/SQL')
def SQL():
    return render_template('SQL.html', f_DIQ=f_DIQ, f_DIR=f_DIR, f_NIQ=f_NIQ, f_NSD=f_NSD, f_batch=f_batch,
                           f_new_BC=f_new_BC, f_change_diq=f_change_diq, dbrestore=dbrestore, dbbackup=dbbackup,
                           service=service)


@app.route('/deploy')
def deploy():
    return render_template('deploy.html',answer=answer,b_version=b_version)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=666, debug=True)
