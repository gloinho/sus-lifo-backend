from flask import Blueprint
from src.api.controllers.patient_controller import patients

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(patients, url_prefix="/patients")
