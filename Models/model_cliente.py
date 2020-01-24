from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField, ReferenceField
)
from Model import Persona

class Cliente(Document):
    
    meta = {'collection': 'cliente'}
    persona = ReferenceField(Persona)
    fecha_ultima_compra = DateTimeField()