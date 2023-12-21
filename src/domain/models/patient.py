from src import db
from sqlalchemy_serializer import SerializerMixin

class Patient(db.Model, SerializerMixin):
    id = db.Column(db.Integer(), primary_key = True, unique=True)
    name = db.Column(db.String(60))
