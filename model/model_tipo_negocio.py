from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    StringField
)

class TipoNegocio(Document):
    
    meta = {'collection': 'tipo_negocio'}
    nombre = StringField()
    nombre_sunat = StringField()