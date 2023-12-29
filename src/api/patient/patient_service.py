from sqlalchemy import desc, update
from src import db
from src.domain.models.patient import Patient
from src.domain.models.schemas import PatientSchema
from werkzeug.exceptions import BadRequest,NotFound

class PatientService:
    @staticmethod
    def getPatients(assisted):
        patient_schema = PatientSchema()
        if(assisted is not None):
            patients = Patient.query.where(Patient.assisted == assisted).order_by(desc(Patient.createdAt)).all()
        else:
            patients = Patient.query.order_by(desc(Patient.createdAt)).all()

        data = [patient_schema.dump(patient) for patient in patients]

        return data
    
    @staticmethod
    def addPatients(request:str):
        patient = Patient(name=request)
        patient_schema = PatientSchema()
        db.session.add(patient)
        db.session.commit()
        return patient_schema.dump(patient)
    
    @staticmethod
    def assistPatient():
        patient:Patient = Patient.query.where(Patient.assisted == False).order_by(desc(Patient.createdAt)).first()

        if patient is None:
            raise BadRequest('All patients were assisted. The line is empty!!! Fala do SUS')
        
        patient.assisted = True
        db.session.commit()

        patient_schema = PatientSchema()
        return patient_schema.dump(patient)


