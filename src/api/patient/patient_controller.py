from flask import request
from flask_restx import Resource
from .patient_dto import PatientDto
from .patient_service import PatientService

api = PatientDto.api

@api.route('/')
class PatientController(Resource):
    @api.doc('Gets the stack of patients.', model=PatientDto.patientResponse)
    @api.response(200, 'Success')
    def get(self):
        return PatientService.getPatients()
    
    @api.doc('Create a new Patient and put him in the top of the stack.', model=PatientDto.patientResponse)
    @api.expect(PatientDto.patientRequest)
    @api.response(200, 'Success')
    def post(self):
        data = request.json
        return PatientService.addPatients(data["name"])
    
    @api.doc('Assist a patient -> remove from the top of the stack.')
    @api.response(200, 'Success')
    def patch(self):
        return PatientService.assistPatient()