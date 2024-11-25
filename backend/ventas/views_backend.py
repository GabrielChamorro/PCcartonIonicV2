# RestFull Basado en Clases
# https://www.django-rest-framework.org/tutorial/3-class-based-views/

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
#from .models import Region,Persona,Comuna
from .models import *
#from .serializers import RegionSerializer,PersonaSerializer
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .negocio import *

# Create your views here.

def indexHarrys(request):
    return HttpResponse("Harrisito El Magnifico, Doble Magnifico")

class JSONResponseOkRows(HttpResponse):
    def __init__(self, data,msg, **kwargs):
        #print(len(data))
        data= {"OK":True,"count":len(data),"registro":data,"msg":msg}
        #print("data",data)
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOkRows, self).__init__(content, **kwargs)


class JSONResponseOk(HttpResponse):
    def __init__(self, data, msg,**kwargs):
        #print("data",data)
        data= {"OK":True,"count":"1","registro":data,"msg":msg}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOk, self).__init__(content, **kwargs)

class JSONResponseErr(HttpResponse):
    def __init__(self, data, **kwargs):
        data= {"OK":False,"count":"0","msg":data}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseErr, self).__init__(content, **kwargs)

#Courrier

class CourrierList(APIView):
    def get(self, request, format=None):
        registros = Courrier.objects.all()
        serializer = CourrierSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.courrierCrear(data['id'], data['precioKM'], data['descripcion'], data['telefono'], data['rut']):
            return JSONResponseErr(None, msg="Error al crear el courrier", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class CourrierDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_Courrier(id)
        serializer = CourrierSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.courrierCrear(id, data['precioKM'], data['descripcion'], data['telefono'], data['rut']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.courrierEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar el courrier", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#MedioDePago


class MedioDePagoList(APIView):
    def get(self, request, format=None):
        registros = MedioDePago.objects.all()
        serializer = MedioDePagoSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.medioDePagoCrear(data['id'], data['nombre'], data['descripcion']):
            return JSONResponseErr(None, msg="Error al crear el medio de pago", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class MedioDePagoDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_MedioDePago(id)
        serializer = MedioDePagoSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.medioDePagoCrear(id, data['nombre'], data['descripcion']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.medioDePagoEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar el medio de pago", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#Factura

class FacturaList(APIView):
    def get(self, request, format=None):
        registros = Factura.objects.all()
        serializer = FacturaSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.facturaCrear(data['id'], data['numeroFactura'], data['fecha'], data['descripcion'], data['idCourrier'], data['idPago'], data['total']):
            return JSONResponseErr(None, msg="Error al crear la factura", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class FacturaDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_Factura(id)
        serializer = FacturaSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.facturaCrear(id, data['numeroFactura'], data['fecha'], data['descripcion'], data['idCourrier'], data['idPago'], data['total']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.facturaEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar la factura", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#TipoDeEnvio


class TipoDeEnvioList(APIView):
    def get(self, request, format=None):
        registros = TipoDeEnvio.objects.all()
        serializer = TipoDeEnvioSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.tipoDeEnvioCrear(data['id'], data['nombre'], data['descripcion']):
            return JSONResponseErr(None, msg="Error al crear el tipo de envío", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class TipoDeEnvioDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_TipoDeEnvio(id)
        serializer = TipoDeEnvioSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.tipoDeEnvioCrear(id, data['nombre'], data['descripcion']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.tipoDeEnvioEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar el tipo de envío", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#Region


class RegionList(APIView):
    def get(self, request, format=None):
        registros = Region.objects.all()
        serializer = RegionSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.regionCrear(data['id'], data['nombre']):
            return JSONResponseErr(None, msg="Error al crear la región", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class RegionDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_Region(id)
        serializer = RegionSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.regionCrear(id, data['nombre']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.regionEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar la región", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#Ciudad


class CiudadList(APIView):
    def get(self, request, format=None):
        registros = Ciudad.objects.all()
        serializer = CiudadSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.ciudadCrear(data['id'], data['nombre'], data['idRegion']):
            return JSONResponseErr(None, msg="Error al crear la ciudad", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class CiudadDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_Ciudad(id)
        serializer = CiudadSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.ciudadCrear(id, data['nombre'], data['idRegion']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.ciudadEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar la ciudad", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#Comuna


class ComunaList(APIView):
    def get(self, request, format=None):
        registros = Comuna.objects.all()
        serializer = ComunaSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.comunaCrear(data['id'], data['nombre'], data['idCiudad']):
            return JSONResponseErr(None, msg="Error al crear la comuna", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class ComunaDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_Comuna(id)
        serializer = ComunaSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.comunaCrear(id, data['nombre'], data['idCiudad']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.comunaEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar la comuna", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#Direccion


class DireccionList(APIView):
    def get(self, request, format=None):
        registros = Direccion.objects.all()
        serializer = DireccionSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.direccionCrear(data['id'], data['nombre'], data['direccion'], data['numero'], data.get('depto', ""), data['idComuna']):
            return JSONResponseErr(None, msg="Error al crear la dirección", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class DireccionDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_Direccion(id)
        serializer = DireccionSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.direccionCrear(id, data['nombre'], data['direccion'], data['numero'], data.get('depto', ""), data['idComuna']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.direccionEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar la dirección", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#Categoria

class CategoriaList(APIView):
    def get(self, request, format=None):
        registros = Categoria.objects.all()
        serializer = CategoriaSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.categoriaCrear(data['id'], data['nombre'], data['descripcion'], data.get('idPadre', None)):
            return JSONResponseErr(None, msg="Error al crear la categoría", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class CategoriaDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_Categoria(id)
        serializer = CategoriaSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.categoriaCrear(id, data['nombre'], data['descripcion'], data.get('idPadre', None)):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.categoriaEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar la categoría", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)

  
#Categoria Empleado

class CategoriaEmpleadoList(APIView):
    def get(self, request, format=None):
        registros = CategoriaEmpleado.objects.all()
        serializer = Negocio.CategoriaEmpleadoSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.categoriaEmpleadoCrear(data['id'], data['nombre'], data['descripcion'], data.get('idPadre', None)):
            return JSONResponseErr(None, msg="Error al crear la categoría del empleado", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class CategoriaEmpleadoDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_CategoriaEmpleado(id)
        serializer = Negocio.CategoriaEmpleadoSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.categoriaEmpleadoCrear(id, data['nombre'], data['descripcion'], data.get('idPadre', None)):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.categoriaEmpleadoEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar la categoría del empleado", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)



#Sucursal

class SucursalList(APIView):
    def get(self, request, format=None):
        registros = Sucursal.objects.all()
        serializer = SucursalSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.sucursalCrear(data['id'], data['nombre'], data['descripcion'], data['direccion']):
            return JSONResponseErr(None, msg="Error al crear la sucursal", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class SucursalDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_Sucursal(id)
        serializer = SucursalSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.sucursalCrear(id, data['nombre'], data['descripcion'], data['direccion']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.sucursalEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar la sucursal", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#Cliente

class ClienteList(APIView):
    def get(self, request, format=None):
        registros = Cliente.objects.all()
        serializer = ClienteSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.clienteCrear(data['id'], data['nombre'], data.get('telefono', ""), data['mail'], data['clave'], data['direccion']):
            return JSONResponseErr(None, msg="Error al crear el cliente", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class ClienteDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_Cliente(id)
        serializer = ClienteSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.clienteCrear(id, data['nombre'], data.get('telefono', ""), data['mail'], data['clave'], data['direccion']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.clienteEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar el cliente", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#Empleado

class EmpleadoList(APIView):
    def get(self, request, format=None):
        registros = Empleado.objects.all()
        serializer = EmpleadoSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.empleadoCrear(data['id'], data['nombre'], data['idCategoria']):
            return JSONResponseErr(None, msg="Error al crear el empleado", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class EmpleadoDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_Cliente(id)
        serializer = EmpleadoSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.empleadoCrear(id, data['nombre'], data['idCategoria']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.empleadoEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar el empleado", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#Usuario

class UsuarioList(APIView):
    def get(self, request, format=None):
        registros = Usuario.objects.all()
        serializer = UsuarioSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.usuarioCrear(data['id'], data['nombre'], data.get('idCliente', None), data.get('idEmpleado', None)):
            return JSONResponseErr(None, msg="Error al crear el usuario", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class UsuarioDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_Usuario(id)
        serializer = UsuarioSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.usuarioCrear(id, data['nombre'], data.get('idCliente', None), data.get('idEmpleado', None)):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.usuarioEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar el usuario", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#Boleta

class BoletaList(APIView):
    def get(self, request, format=None):
        registros = Boleta.objects.all()
        serializer = BoletaSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.boletaCrear(data['id'], data['numeroBoleta'], data['fecha'], data['descripcion'], data['idCliente'], data['idEmpleado'], data['idPago'], data['total']):
            return JSONResponseErr(None, msg="Error al crear la boleta", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class BoletaDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_Boleta(id)
        serializer = BoletaSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.boletaCrear(id, data['numeroBoleta'], data['fecha'], data['descripcion'], data['idCliente'], data['idEmpleado'], data['idPago'], data['total']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.boletaEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar la boleta", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#BoletaDetalle

class BoletaDetalleList(APIView):
    def get(self, request, format=None):
        registros = BoletaDetalle.objects.all()
        serializer = BoletaDetalleSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.boletaDetalleCrear(data['id'], data['fecha'], data['descripcion'], data['idProducto'], data['idEnvio'], data['idBoleta'], data['total'], data['cantidad'], data['precio']):
            return JSONResponseErr(None, msg="Error al crear el detalle de boleta", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class BoletaDetalleDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_BoletaDetalle(id)
        serializer = BoletaDetalleSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.boletaDetalleCrear(id, data['fecha'], data['descripcion'], data['idProducto'], data['idEnvio'], data['idBoleta'], data['total'], data['cantidad'], data['precio']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.boletaDetalleEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar el detalle de boleta", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)



#Compra


class CompraList(APIView):
    def get(self, request, format=None):
        registros = Compra.objects.all()
        serializer = CompraSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.compraCrear(data['id'], data['numeroBoleta'], data['fecha'], data['descripcion'], data['idCliente'], data['idEmpleado'], data['idPago'], data['idCourrier'], data['total']):
            return JSONResponseErr(None, msg="Error al crear la compra", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class CompraDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_Compra(id)
        serializer = CompraSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.compraCrear(id, data['numeroBoleta'], data['fecha'], data['descripcion'], data['idCliente'], data['idEmpleado'], data['idPago'], data['idCourrier'], data['total']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.compraEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar la compra", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


#CompraDetalle

class CompraDetalleList(APIView):
    def get(self, request, format=None):
        registros = CompraDetalle.objects.all()
        serializer = CompraDetalleSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.compraDetalleCrear(data['id'], data['fecha'], data['descripcion'], data['idProducto'], data['idEnvio'], data['idCompra'], data['total'], data['cantidad'], data['precio']):
            return JSONResponseErr(None, msg="Error al crear el detalle de compra", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class CompraDetalleDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_CompraDetalle(id)
        serializer = CompraDetalleSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.compraDetalleCrear(id, data['fecha'], data['descripcion'], data['idProducto'], data['idEnvio'], data['idCompra'], data['total'], data['cantidad'], data['precio']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.compraDetalleEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar el detalle de compra", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)

#Compra carrito

class CompraCarritoList(APIView):
    def get(self, request, format=None):
        registros = CompraCarrito.objects.all()
        serializer = CompraCarritoSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.compraCarritoCrear(data['id'], data['fecha'], data['descripcion'], data['idProducto'], data['idEnvio'], data['total'], data['cantidad'], data['precio']):
            return JSONResponseErr(None, msg="Error al crear el carrito de compra", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class CompraCarritoDetail(APIView):
    def get(self, request, id, format=None):
        registro = Negocio.get_CompraCarrito(id)
        serializer = CompraCarritoSerializer(registro)
        return JSONResponseOk(serializer.data, msg="")

    def put(self, request, id, format=None):
        data = JSONParser().parse(request)
        if not Negocio.compraCarritoCrear(id, data['fecha'], data['descripcion'], data['idProducto'], data['idEnvio'], data['total'], data['cantidad'], data['precio']):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        if not Negocio.compraCarritoEliminar(id):
            return JSONResponseErr(None, msg="Error al eliminar el carrito de compra", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


##PRODUCTO

class ProductoList(APIView):
    ##permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        registros = Producto.objects.all()
        serializer = ProductoSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.productoCrear(data['id'], data['nombre'], data['descripcion'], data['imagenPrincipal'], data['precio'], data['stock'], data['idCategoria']):
            return JSONResponseErr(None, msg="Error al crear el producto", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class ProductoListxx(APIView):
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        print("1",data['id'])
        print("2",data['nombre'])
        print("3",data['descripcion'])
        print("4",data['imagenPrincipal'])
        print("5",data['precio'])
        print("6",data['stock'])
        print("7",data['idCategoria'])

        if (not Negocio.productoCrear(data['id'],
                                data['nombre'], data['descripcion'], data['imagenPrincipal'], data['precio'], data['stock'], data['idCategoria'])):
            return JSONResponseErr(None, msg="Error al crear el producto", status=status.HTTP_400_BAD_REQUEST)
        print("hola 22",data)    
        return JSONResponseOk(None,msg="Registro Actualizado")

class ProductoDetail(APIView):
    def get(self, request,id,format=None):
        registro = Negocio.productoGet(id)
        serializer = ProductoSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")
    
    def put(self, request,id,format=None):
        data = JSONParser().parse(request)
        print("hola modificar",data)
        if (not Negocio.productoCrear(id,
                                data['nombre'], data['descripcion'], data['imagenPrincipal'], data['precio'], data['stock'], data['idCategoria'])):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None,msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        print("hola delete1")
        if (not Negocio.productoEliminar(id)):
            return JSONResponseErr(None, msg="Error al eliminar el producto", status=status.HTTP_400_BAD_REQUEST)
        print("hola delete2")
        return Response(status=status.HTTP_204_NO_CONTENT)       









    
# from rest_framework_simplejwt.tokens import RefreshToken

# class LoginView(APIView):
#     def post(self, request):
#         # Perform authentication checks here

#         # Generate tokens
#         refresh = RefreshToken.for_user("user")
#         access_token = str(refresh.access_token)

#         return Response({'access_token1': access_token})