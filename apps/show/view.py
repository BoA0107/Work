from flask import *

show_bp = Blueprint('show', __name__)

@show_bp.route('/')
def show():
    return 'show page'


# @app.route('/')
# def show():
#     return render_template('show.html')
