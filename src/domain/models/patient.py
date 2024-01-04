from datetime import datetime
from sqlalchemy.sql import func
from src import db
from sqlalchemy_serializer import SerializerMixin

class Patient(db.Model, SerializerMixin):
    id = db.Column(db.Integer(), primary_key = True, unique=True)
    name = db.Column(db.String(60))
    createdAt = db.Column(db.DateTime(timezone=True), server_default= func.now())
    updatedAt = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    assisted = db.Column(db.Boolean(), default=False)

    def __init__(self, name, createdAt = datetime.utcnow(), assisted=False):
        self.name = name
        self.assisted = assisted
        self.createdAt = createdAt
