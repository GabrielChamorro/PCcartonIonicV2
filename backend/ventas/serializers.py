from rest_framework import serializers
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CourrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courrier
        fields = '__all__'


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'
                


#ch
class MedioDePagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedioDePago
        fields = '__all__'

#ch
class TipoDeEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDeEnvio
        fields = '__all__'

#ch
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

#ch
class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

#ch
class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'

#ch
class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

#ch
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

#ch
class CategoriaEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaEmpleado
        fields = '__all__'

#ch
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ViewProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
       # fields = ('id','nombre','descripcion','precio','stock','idCategoria')
        fields = '__all__'

#ch
class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'

#ch
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

#ch
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

#ch
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'




#jp
class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'

#jp
class BoletaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoletaDetalle
        fields = '__all__'

#jp       
class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'

#jp
class CompraDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraDetalle
        fields = '__all__'

#jp
class CompraCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraCarrito
        fields = '__all__'




class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'
