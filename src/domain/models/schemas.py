from src import ma

class PatientSchema(ma.Schema):
    class Meta:
        fields = ("id","name", "createdAt", "assisted", "updatedAt")
