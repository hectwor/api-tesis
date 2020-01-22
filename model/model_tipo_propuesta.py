from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    StringField
)

class TipoPropuesta(Document):
    
    meta = {'collection': 'tipo_propuesta'}
    nombre = StringField()
    tiempo_evaluacion = StringField()
    algoritmo_usado = StringField()