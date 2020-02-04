from Models.model_persona import Persona
from Models.model_rol import Rol
from Models.model_usuario import Usuario
from Models.model_proveedor import (Proveedor, ProveedorInput)
from Models.model_categoria_producto import (CategoriaProducto, CategoriaProductoInput)
from Models.model_producto import (Producto, ProductoInput)
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
    CategoriaProductoInput,
    Cliente,
    Compra,
    DetalleCompra,
    DetalleVenta,
    Negocio,
    Persona,
    Producto,
    ProductoInput,
    Propuesta,
    Proveedor,
    ProveedorInput,
    Rol,
    TipoNegocio,
    TipoPropuesta,
    Trabajador,
    Usuario,
    Venta
}