from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    ReferenceField, StringField
)
from model.model_usuario import Usuario

class Persona(Document):
    
    meta = {'collection': 'persona'}
    usuario = ReferenceField(Usuario)
    estado = StringField()
    token = StringField()