from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.config.config import Config
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

config = Config().dev_config

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI_DEV")

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from src.api.routes.routes import api

app.register_blueprint(api, url_prefix="/api")

from src.domain.models.patient import Patient