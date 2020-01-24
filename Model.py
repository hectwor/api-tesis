from Models.model_persona import Persona
from Models.model_rol import Rol
from Models.model_usuario import Usuario
from Models.model_proveedor import Proveedor
from Models.model_categoria_producto import CategoriaProducto
from Models.model_producto import Producto
from Models.model_administrador_negocio import AdministradorNegocio
from Models.model_cliente import Cliente
from Models.model_compra import Compra
from Models.model_detalle_compra import DetalleCompra
from Models.model_venta import Venta
from Models.model_detalle_venta import DetalleVenta
from Models.model_tipo_negocio import TipoNegocio
from Models.model_negocio import Negocio
from Models.model_propuesta import Propuesta
from Models.model_tipo_propuesta import TipoPropuesta
from Models.model_trabajador import Trabajador

Model = {
    AdministradorNegocio,
    CategoriaProducto,
    Cliente,
    Compra,
    DetalleCompra,
    DetalleVenta,
    Negocio,
    Persona,
    Producto,
    Propuesta,
    Proveedor,
    Rol,
    TipoNegocio,
    TipoPropuesta,
    Trabajador,
    Usuario,
    Venta
}