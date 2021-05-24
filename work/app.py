# -*- coding:utf-8 -*-

from flask import *

app = Flask(__name__)


@app.route('/')
def show():
    return render_template("show.html")


if __name__ == "__main__":
    app.run(debug=True)
