import re
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
        if not request: 
            raise BadRequest("Nome do paciente não pode ser vazio ou nulo")
        
        if re.match(r"^[a-zA-ZÀ-ÖØ-öø-ÿ]+$", request ) is None:
            raise BadRequest("Nomes podem conter apenas letras.")
        

        patient = Patient(name=request)
        patient_schema = PatientSchema()
        db.session.add(patient)
        db.session.commit()
        return patient_schema.dump(patient)
    
    @staticmethod
    def assistPatient():
        patient:Patient = Patient.query.where(Patient.assisted == False).order_by(desc(Patient.createdAt)).first()

        if patient is None:
            raise BadRequest('Todos os pacientes foram atendidos, a fila está vazia.')
        
        patient.assisted = True
        db.session.commit()

        patient_schema = PatientSchema()
        return patient_schema.dump(patient)


