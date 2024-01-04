from datetime import datetime
import logging
from src import db
from src.domain.models.patient import Patient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def seed_data():
    if not Patient.query.first():
        db.create_all()

        patients_data = [
                            {"name": "Jere", "createdAt": datetime(2023, 5, 12, 8, 30)},
                            {"name": "Abram", "createdAt": datetime(2022, 9, 18, 15, 45)},
                            {"name": "Pattie", "createdAt": datetime(2024, 1, 2, 12, 20)},
                            {"name": "Amy", "createdAt": datetime(2023, 11, 7, 9, 10)},
                            {"name": "Base", "createdAt": datetime(2022, 7, 30, 18, 55)},
                            {"name": "Daffie", "createdAt": datetime(2023, 3, 22, 14, 0)},
                            {"name": "Iolanthe", "createdAt": datetime(2022, 12, 14, 11, 25)},
                        ]

        for data in patients_data:
            patient = Patient(**data)
            db.session.add(patient)

        db.session.commit()

        logger.info("Dados de pacientes inseridos com sucesso.")
    else:
        logger.info("O banco de dados já contém dados. O seed não será executado.")
