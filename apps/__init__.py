from flask import *
from apps.show.view import show_bp
def create_app():
    app=Flask(__name__)
    app.register_blueprint(show_bp)