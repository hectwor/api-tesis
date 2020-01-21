from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    ReferenceField, IntField, FloatField
)
from model.model_usuario import Usuario
from model.model_negocio import Negocio

class Trabajador(Document):
    
    meta = {'collection': 'trabajador'}
    negocio = ReferenceField(Negocio)
    usuario = ReferenceField(Usuario)
    horas_trabajadas = IntField()
    sueldo_actual_mensual = FloatField()