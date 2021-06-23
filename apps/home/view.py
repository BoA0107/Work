from flask import *

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    return 'home'