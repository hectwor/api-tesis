from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    ReferenceField, StringField
)
from model.model_venta import Venta

class DetalleVenta(Document):
    
    meta = {'collection': 'detalle_venta'}
    venta = ReferenceField(Venta)
    descripcion = StringField()
    estado = StringField()