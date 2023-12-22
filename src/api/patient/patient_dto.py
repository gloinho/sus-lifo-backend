from flask_restx import Namespace, fields

class PatientDto:
    api = Namespace("patients",description='Patients related operations' )

    patientRequest = api.model('Patient Request',
                               {'name': fields.String(required=True, description='The patient name')})


    patientResponse = api.model('Patient Response', {
        'id': fields.String(description='The patient identifier'),
        'name': fields.String(description='The patient name'),
        'createdAt': fields.DateTime(description='The date the patient entered the queue'),
        'updatedAt': fields.DateTime(description='The date of the patient last update.'),
        'assisted': fields.Boolean(description='The status of the patient in queue.'),
    })