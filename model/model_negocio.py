from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    ReferenceField, StringField, IntField, BooleanField
)
from model.model_tipo_negocio import TipoNegocio

class Negocio(Document):
    
    meta = {'collection': 'negocio'}
    nombre = StringField()
    tipo_negocio = ReferenceField(TipoNegocio)
    nro_trabajadores = IntField()
    esta_en_sunat = BooleanField()