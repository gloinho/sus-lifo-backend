from flask import Flask
from .config import config_by_name
from .extensions import db, ma
from flask_cors import CORS

def create_app(config_name):

    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_by_name[config_name])

    register_extensions(app)

    from .api import api_bp
    app.register_blueprint(api_bp)

    return app


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)