from func.func_home import *
from func.func_BCA import *
from func.func_SQL import *

app = Flask(__name__)


@app.route('/')
def show():
    return render_template('show.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template("home.html", plan_info=plan_info, links=links_dct, career_level=career_level)


@app.route('/BCA')
def BCA():
    return render_template('BCA.html', UAT_BC=UAT_BC)


@app.route('/SQL')
def SQL():
    return render_template('SQL.html', f_DIQ=f_DIQ, f_DIR=f_DIR, f_NIQ=f_NIQ, f_NSD=f_NSD, f_batch=f_batch,f_new_BC=f_new_BC,f_change_diq=f_change_diq)


@app.route('/deploy')
def deploy():
    return render_template('deploy.html')


if __name__ == "__main__":
    app.run(port=7777, debug=True)
