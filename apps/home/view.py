from flask import *

user_bp = Blueprint('home', __name__)

@user_bp.route('/home')
def home():
    return 'home'