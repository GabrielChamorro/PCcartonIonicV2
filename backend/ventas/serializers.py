from rest_framework import serializers
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#ch
class MedioDePagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedioDePago
        fields = ('id','nombre', 'descripcion')

#ch
class TipoDeEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDeEnvio
        fields = ('id','nombre', 'descripcion')

#ch
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id','nombre')

#ch
class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id','nombre','idRegion')

#ch
class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('id','nombre','idCiudad')

#ch
class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('id','nombre','direccion','numero','depto','idComuna')

#ch
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','nombre','descripcion','idPadre')

#ch
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','nombre','descripcion','precio','stock','idCategoria')
        #fields = '__all__'

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
        fields = ('id', 'numeroBoleta','fecha','descripcion','idCliente','idEmpleado', 'idPago', 'total')

#jp
class BoletaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoletaDetalle
        fields = ('id', 'fecha','descripcion','idProducto','idEnvio','total','cantidad','precio')

#jp       
class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ('id', 'numeroBoleta','fecha','descripcion','idCliente','idEmpleado', 'idPago', 'total')

#jp
class CompraDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraDetalle
        fields = ('id', 'fecha','descripcion','idProducto','idEnvio','total','cantidad','precio')

#jp
class CompraCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraCarrito
        fields = ('id', 'fecha','descripcion','idProducto','idEnvio','total','cantidad','precio')

class Usuario2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario2
        fields = ['id', 'nombre', 'clave']
##AAAA


class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'


'''
class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('idGenero','codigo', 'nombre')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('idRegion','codigo', 'nombre')

class RegionSerializerPutDelRead(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('codigo', 'nombre')        

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('idProvincia','codigo', 'nombre','region')

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('idComuna','codigo', 'nombre','provincia')

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('rut', 'dv', 'fechaNacimiento', 'nombre', 'papellido', 'sapellido', 'email','comuna','genero')
class ViewClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewCliente
        fields = ('rut', 'dv',  'nombre', 'papellido', 'sapellido', 'email','comuna','genero')

class PerroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perro
        fields = ('IdPerro','nombre', 'descripcion', 'raza')   
class ViewPerroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewPerro
        fields = ('IdPerro','nombre', 'descripcion', 'raza')   
'''