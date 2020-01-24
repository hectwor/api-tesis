from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    ReferenceField, StringField
)

class Persona(Document):
    
    meta = {'collection': 'persona'}
    nombre = StringField()
    apellido_paterno = StringField()
    apellido_materno = StringField()
    tipo_documento = StringField()
    documento = StringField()
    sexo = StringField()
    telefono = StringField()
    email = StringField()