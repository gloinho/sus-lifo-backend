from flask import Blueprint, request
from src.api.services.patient_service import addPatients, getPatients

patients = Blueprint("patients", __name__)

@patients.route('/', methods = ["POST"])
def addPatientsAction():
    data = request.json
    return addPatients(data["name"])

@patients.route('/', methods = ["GET"])
def getPatientsAction():
    return getPatients()
