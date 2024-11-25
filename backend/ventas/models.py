from django.db import models

# Create your models here.

class Courrier(models.Model):
    id = models.AutoField(primary_key=True)
    precioKM = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'courrier'



class MedioDePago(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'medioDePago'


class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    numeroFactura = models.CharField(max_length=50)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)
    idCourrier = models.ForeignKey(Courrier, on_delete=models.CASCADE, db_column='idCourrier')
    idPago = models.ForeignKey(MedioDePago, on_delete=models.CASCADE, db_column='idPago')
    total = models.IntegerField()
    
    class Meta:
        db_table = 'factura'



class TipoDeEnvio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'tipoDeEnvio'

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'region'


class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    idRegion = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='idRegion')
    
    class Meta:
        db_table = 'ciudad'


class Comuna(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    idCiudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, db_column='idCiudad')        
    
    class Meta:
        db_table = 'comuna'


class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    numero = models.CharField(max_length=50)
    depto = models.CharField(max_length=50, blank=True)
    idComuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, db_column='idComuna')
    
    class Meta:
        db_table = 'direccion'


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    idPadre = models.ForeignKey('self', null=True, on_delete=models.CASCADE, db_column='idPadre')
    
    class Meta:
        db_table = 'categoria'

class CategoriaEmpleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    idPadre = models.ForeignKey('self', null=True, on_delete=models.CASCADE, db_column='idPadre')
    
    class Meta:
        db_table = 'categoriaEmpleado   '


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    imagenPrincipal = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='idCategoria')
    
    class Meta:
        db_table = 'Producto'


class Sucursal(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, db_column='idDireccion')
    
    class Meta:
        db_table = 'sucursal'


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, blank=True)
    mail = models.CharField(max_length=100)
    clave = models.CharField(max_length=50)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, db_column='idDireccion')
    
    class Meta:
        db_table = 'cliente'


class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='idCategoria')
    
    class Meta:
        db_table = 'empleado'





class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    idCliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE, db_column='idCliente')
    idEmpleado = models.ForeignKey(Empleado, null=True, on_delete=models.CASCADE, db_column='idEmpleado')
    
    class Meta:
        db_table = 'usuario'


class Boleta(models.Model):
    id = models.AutoField(primary_key=True)
    numeroBoleta = models.CharField(max_length=50)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='idCliente')
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='idEmpleado')
    idPago = models.ForeignKey(MedioDePago, on_delete=models.CASCADE, db_column='idPago')
    total = models.IntegerField()
    
    class Meta:
        db_table = 'boleta'


class BoletaDetalle(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='idProducto')
    idEnvio = models.ForeignKey('TipoDeEnvio', on_delete=models.CASCADE, db_column='idEnvio')
    idBoleta = models.ForeignKey('Boleta', on_delete=models.CASCADE, db_column='idBoleta')
    total = models.IntegerField()
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    
    class Meta:
        db_table = 'boletaDetalle'


class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    numeroBoleta = models.CharField(max_length=50)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='idCliente')
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='idEmpleado')
    idPago = models.ForeignKey('MedioDePago', on_delete=models.CASCADE, db_column='idPago')
    idCourrier = models.ForeignKey(Courrier, on_delete=models.CASCADE, db_column='idCourrier')
    total = models.IntegerField()
    
    class Meta:
        db_table = 'compra'


class CompraDetalle(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='idProducto')
    idEnvio = models.ForeignKey('TipoDeEnvio', on_delete=models.CASCADE, db_column='idEnvio')
    idCompra = models.ForeignKey('Compra', on_delete=models.CASCADE, db_column='idCompra')
    total = models.IntegerField()
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    
    class Meta:
        db_table = 'compraDetalle'


class CompraCarrito(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='idProducto')
    idEnvio = models.ForeignKey('TipoDeEnvio', on_delete=models.CASCADE, db_column='idEnvio')
    total = models.IntegerField()
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    
    class Meta:
        db_table = 'compraCarrito'







def cargarFoto(instance, filename):
    return "fotos/foto_{0}_{1}".format(instance.rut, filename )