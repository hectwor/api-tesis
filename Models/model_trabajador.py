from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    ReferenceField, IntField, FloatField
)
from Model import Usuario, Negocio

class Trabajador(Document):
    
    meta = {'collection': 'trabajador'}
    negocio = ReferenceField(Negocio)
    usuario = ReferenceField(Usuario)
    horas_trabajadas = IntField()
    sueldo_actual_mensual = FloatField()