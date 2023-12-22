from flask_restx import Api
from flask import Blueprint
from .patient.patient_controller import api as patient_namespace

api_bp = Blueprint("api", __name__)

api = Api(api_bp,
        title='SUS-LIFO-API',
        version='1.0',
        description='',
        prefix='/api/v1')

# API namespaces
api.add_namespace(patient_namespace)