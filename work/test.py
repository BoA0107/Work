from flask import Flask
from flask import render_template
import os
app = Flask(__name__)


basedir=os.path.abspath(os.path.dirname(__file__))
file_path= basedir + "/static" + "BCA_01.png"


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)