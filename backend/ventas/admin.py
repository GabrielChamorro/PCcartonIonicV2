from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(MedioDePago)
admin.site.register(TipoDeEnvio)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Sucursal)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Usuario)
admin.site.register(Boleta)
admin.site.register(BoletaDetalle)
admin.site.register(Compra)
admin.site.register(CompraDetalle)
admin.site.register(CompraCarrito)
