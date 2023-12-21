from src import db
from src.domain.models.patient import Patient


def getPatients():
    patients = Patient.query.all()
    patients_lifo = list(reversed(patients))
    serialized_patients = [patient.to_dict() for patient in patients_lifo]

    return serialized_patients

def addPatients(request):
    patient = Patient(name=request)
    db.session.add(patient)
    db.session.commit()
    return patient.to_dict()