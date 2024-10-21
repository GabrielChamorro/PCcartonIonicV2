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


class GeneroList(APIView):
    def get(self, request, format=None):
         registro = Genero.objects.all()
         serializer = GeneroSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

class RegionList(APIView):
    def get(self, request, format=None):
         registro = Region.objects.all()
         serializer = RegionSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    
class ProvinciaList(APIView):
    def get(self, request,region, format=None):
         #registro = Provincia.objects.all()
         #registro = Provincia.objects.get(region=region) #para Obtener un registro
         registro = Provincia.objects.filter(region=region) # Filtrar por un campo
         serializer = ProvinciaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    
class ComunaList(APIView):
    def get(self, request,provincia, format=None):
         #registro = Comuna.objects.all()
         registro = Comuna.objects.filter(provincia=provincia) # Filtrar por un campo
         serializer = ComunaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

class PersonaList(APIView):
    def get(self, request, format=None):
         registro = Persona.objects.all()
         serializer = PersonaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
         #return Response(serializer.data)

    def post(self, request, format=None):
        #print("1,Post",request)
        # insert en la tabla cliente
        # insert en la tabla usuario
        data = JSONParser().parse(request)
        #print("1",data)
        registro = PersonaSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            # Enviar harrys
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
class PersonaDetail(APIView):
    def get_object(self, pk):
        try:
            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = PersonaSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = PersonaSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

#################      CON NEGOCIO, más ordenado
from rest_framework.permissions import IsAuthenticated
from .negocio import *
class ClienteList(APIView):
    ##permission_classes = (IsAuthenticated,)
#### Observe que  clienteCrear se llama dos veces en el post y en el Put
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if (not Negocio.clienteCrear(data['rut'],data['dv']
                            ,data['nombre'],data['papellido'],data['sapellido']
                            ,data['email']
                            ,data['comuna'],data['genero'])):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None,msg="Resistro Actualizado")
from django.http import JsonResponse    
class ClienteDetail(APIView):
    ##permission_classes = (IsAuthenticated,)
    
    def get(self, request, rut, format=None):
        registro = Negocio.clienteGet(rut)
        serializer = ViewClienteSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")
    
#### Observe que  clienteCrear se llama dos veces en el post y en el Put
    def put(self, request,rut, format=None):
        data = JSONParser().parse(request)
        if (not Negocio.clienteCrear(data['rut'],data['dv']
                            ,data['nombre'],data['papellido'],data['sapellido']
                            ,data['email']
                            ,data['comuna'],data['genero'])):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None,msg="Resistro Actualizado")

    def delete(self, request, rut, format=None):
        if (not Negocio.clienteEliminar(rut)):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_204_NO_CONTENT)   
    


####PERROLIST

def JSONResponseOk(data, msg="", status=status.HTTP_200_OK):
    return JsonResponse({"message": msg, "data": data}, status=status)

def JSONResponseErr(data, msg="", status=status.HTTP_400_BAD_REQUEST):
    return JsonResponse({"message": msg, "data": data}, status=status)

class PerroList(APIView):
    ##permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.perroCrear(data['IdPerro'], data['nombre'], data['descripcion'], data['raza']):
            return JSONResponseErr(None, msg="Error al crear el perro", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class PerroList(APIView):
    ##permission_classes = (IsAuthenticated,)
    #### Observe que  clienteCrear se llama dos veces en el post y en el Put
    def post(self, request, format=None):
        print("hola")
        data = JSONParser().parse(request)
        print("hola 1")
        print("1",data['IdPerro'])
        print("3",data['nombre'])
        print("4",data['descripcion'])
        print("5",data['raza'])

        if (not Negocio.perroCrear(data['IdPerro'],
                                data['nombre'],data['descripcion'],data['raza'])):
            return JSONResponseErr(None, msg="Error al crear el perro", status=status.HTTP_400_BAD_REQUEST)
        print("hola 22",data)    
        return JSONResponseOk(None,msg="Registro Actualizado")

class PerroDetail(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request,IdPerro,format=None):
        registro = Negocio.perroGet(IdPerro)
        serializer = ViewPerroSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")
    
    #### Observe que  clienteCrear se llama dos veces en el post y en el Put
    def put(self, request,IdPerro,format=None):
        data = JSONParser().parse(request)
        print("hola modificar")
        if (not Negocio.perroCrear(data['IdPerro']
                            ,data['nombre'],data['descripcion'],data['raza'])):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None,msg="Registro Actualizado")

    def delete(self, request, IdPerro, format=None):
        print("hola delete1")
        if (not Negocio.perroEliminar(IdPerro)):
            return JSONResponseErr(None, msg="Error al eliminar el perro", status=status.HTTP_400_BAD_REQUEST)
        print("hola delete2")
        return Response(status=status.HTTP_204_NO_CONTENT)       



##AAAA
class BoletaList(APIView):
    def get(self, request, format=None):
        boletas = Boleta.objects.all()
        serializer = BoletaSerializer(boletas, many=True)
        return JSONResponseOkRows(serializer.data, "")




##PRODUCTO

class ProductoList(APIView):
    ##permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        registros = Producto.objects.all()
        serializer = ProductoSerializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.productoCrear(data['id'], data['nombre'], data['descripcion'], data['precio'], data['stock'], data['idCategoria']):
            return JSONResponseErr(None, msg="Error al crear el producto", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)

class ProductoListxx(APIView):
    ##permission_classes = (IsAuthenticated,)
    #### Observe que  clienteCrear se llama dos veces en el post y en el Put
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        print("1",data['id'])
        print("2",data['nombre'])
        print("3",data['descripcion'])
        print("4",data['precio'])
        print("5",data['stock'])
        print("6",data['idCategoria'])

        if (not Negocio.productoCrear(data['id'],
                                data['nombre'], data['descripcion'], data['precio'], data['stock'], data['idCategoria'])):
            return JSONResponseErr(None, msg="Error al crear el producto", status=status.HTTP_400_BAD_REQUEST)
        print("hola 22",data)    
        return JSONResponseOk(None,msg="Registro Actualizado")

class ProductoDetail(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request,id,format=None):
        registro = Negocio.productoGet(id)
        serializer = ViewproductoSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")
    
    #### Observe que  clienteCrear se llama dos veces en el post y en el Put
    def put(self, request,id,format=None):
        data = JSONParser().parse(request)
        print("hola modificar",data)
        if (not Negocio.productoCrear(id,
                                data['nombre'], data['descripcion'], data['precio'], data['stock'], data['idCategoria'])):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None,msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        print("hola delete1")
        if (not Negocio.productoEliminar(id)):
            return JSONResponseErr(None, msg="Error al eliminar el producto", status=status.HTTP_400_BAD_REQUEST)
        print("hola delete2")
        return Response(status=status.HTTP_204_NO_CONTENT)       


##Usuario2 GB CH, tiene: id ,nombre,clave

class Usuario2List(APIView):
    def get(self, request, format=None):
        registros = Usuario2.objects.all()
        serializer = Usuario2Serializer(registros, many=True)
        return JSONResponseOkRows(serializer.data, "")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if not Negocio.usuario2Crear(data['id'], data['nombre'], data['clave']):
            return JSONResponseErr(None, msg="Error al crear el usuario", status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None, msg="Registro Creado", status=status.HTTP_201_CREATED)
    
class Usuario2Listxx(APIView):
    ##permission_classes = (IsAuthenticated,)
    #### Observe que  clienteCrear se llama dos veces en el post y en el Put
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        print("1",data['id'])
        print("2",data['nombre'])
        print("3",data['clave'])

        if (not Negocio.usuario2Crear(data['id'],
                                data['nombre'], data['clave'])):
            return JSONResponseErr(None, msg="Error al crear el usuario", status=status.HTTP_400_BAD_REQUEST)
        print("hola 22",data)    
        return JSONResponseOk(None,msg="Registro Actualizado")
    
class Usuario2Detail(APIView):
    def get(self, request,id,format=None):
        registro = Negocio.usuario2Get(id)
        serializer = ViewUsuario2Serializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")
    
    #### Observe que  clienteCrear se llama dos veces en el post y en el Put
    def put(self, request,id,format=None):
        data = JSONParser().parse(request)
        print("hola modificar",data)
        if (not Negocio.usuario2Crear(id,
                                data['nombre'], data['clave'])):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None,msg="Registro Actualizado")

    def delete(self, request, id, format=None):
        print("hola delete1")
        if (not Negocio.usuario2Eliminar(id)):
            return JSONResponseErr(None, msg="Error al eliminar el usuario", status=status.HTTP_400_BAD_REQUEST)
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