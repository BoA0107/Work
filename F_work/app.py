# -*- coding:utf-8 -*-

from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")