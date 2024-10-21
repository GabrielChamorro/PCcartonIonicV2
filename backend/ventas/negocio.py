from .models import *
class Negocio:
    # Metodos Státicos no necesitan ==> self
    def get_viewcliente( rut):
        try:
            return ViewCliente.objects.get(pk=rut)
        except ViewCliente.DoesNotExist:
            raise None
    def get_cliente( rut):
        try:
            return Cliente.objects.get(pk=rut)
        except Cliente.DoesNotExist:
            return None             
    def get_persona( rut):
        try:
            return Persona.objects.get(pk=rut)
        except Persona.DoesNotExist:
            return None       
    def get_usuario( usuario):
        try:
            usuarios = Usuario.objects.filter(usuario=usuario)
            if (usuarios.count()> 0):
                return usuarios[0]
            else:
                return None
        except Usuario.DoesNotExist:
            return None
               
    def clienteCrear(rut,dv,nombres,paterno,materno,email,comuna,genero):
        persona = Negocio.get_persona(int(rut))
        cliente = Negocio.get_cliente(rut)
        usuario = Negocio.get_usuario(rut)
        if (persona== None):
            persona =  Persona(rut,dv,nombres,paterno,materno,email,'2023-01-01','2023-01-01',comuna,genero,1)
        else:
            persona.nombre=nombres

        # No tienen mucho sentido solo es para el ejemplo
        if (cliente== None):
            cliente = Cliente(rut,None,'2023-01-01',0)
        if (usuario== None):
            usuario = Usuario(None,rut,rut,rut)
        persona.save()
        cliente.save()
        usuario.save()
        return True


    def clienteGet(rut):
        return Negocio.get_viewcliente(rut)
    
    def clienteEliminar(rut):
        persona = Negocio.get_persona(int(rut))
        cliente = Negocio.get_cliente(rut)
        usuario = Negocio.get_usuario(rut)
        ###  Recuerde que no debiera eliminar, mejor desactivar el registro
        usuario.delete()
        cliente.delete()
        persona.delete()    

    
    
    ###Perro

    def get_viewperro(IdPerro):
        try:
            return ViewPerro.objects.get(pk=IdPerro)
        except ViewPerro.DoesNotExist:
            raise None
    def get_Perro(IdPerro):
        try:
            return Perro.objects.get(pk=IdPerro)
        except Perro.DoesNotExist:
            return None 

    def perroCrear(IdPerro,Nombre,Descripcion,Raza):
        print ("perroCrear2")
        perro = Negocio.get_Perro(int(IdPerro))
        print ("perroCrear3")
        if (perro== None):
            print ("perroCrear4")
            perro =  Perro(IdPerro,Nombre,Descripcion,Raza)
        else:
            print ("perroCrear5")
            perro.nombre=Nombre

        # No tienen mucho sentido solo es para el ejemplo
        #if (cliente== None):
            #cliente = Cliente(IdPerro,None,'2023-01-01',0)
        #if (usuario== None):
            #usuario = Usuario(None,IdPerro,IdPerro,IdPerro)
        perro.save()
        return True


    def perroGet(IdPerro):
        return Negocio.get_viewperro(IdPerro)
    
    def perroEliminar(IdPerro):
        print("hola PerroEliminar1")
        perro = Negocio.get_Perro(int(IdPerro))
        print("hola PerroEliminar2")
        ###  Recuerde que no debiera eliminar, mejor desactivar el registro

        perro.delete() 


#Producto GB CH
    def get_viewProducto(id):
        try:
            return ViewProducto.objects.get(pk=id)
        except ViewProducto.DoesNotExist:
            raise None
    def get_Producto(id):
        try:
            return Producto.objects.get(pk=id)
        except Producto.DoesNotExist:
            return None 
    
    def productoCrear(id, nombre, descripcion, precio, stock, idCategoria):
        producto = Negocio.get_Producto(int(id))
        if (producto== None):
            try:
                precio = int(precio)
                if precio > 25:
                    producto = Producto(id, nombre, descripcion, precio, stock, idCategoria)
                else:
                    raise ValueError("El precio debe ser mayor a 25")
            except ValueError:
                raise ValueError("El precio debe ser un numero")
        else:
            producto.nombre = nombre
            producto.descripcion = descripcion
            producto.precio = precio
            producto.stock = stock
            clCategoria = Categoria(idCategoria)
            producto.idCategoria = clCategoria
        print("producto", producto)
        # No tienen mucho sentido solo es para el ejemplo
        #if (cliente== None):
            #cliente = Cliente(IdPerro,None,'2023-01-01',0)
        #if (usuario== None):
            #usuario = Usuario(None,IdPerro,IdPerro,IdPerro)
        producto.save()
        return True


    def productoGet(id):
        return Negocio.get_viewProducto(id)
    
    def productoEliminar(id):
        producto = Negocio.get_Producto(int(id))
        ###  Recuerde que no debiera eliminar, mejor desactivar el registro

        producto.delete() 

#Usuario2 GB CH

    def get_viewUsuario2(id):
        try:
            return ViewUsuario2.objects.get(pk=id)
        except ViewUsuario2.DoesNotExist:
            raise None
    
    def get_Usuario2(id):   
        try:
            return Usuario2.objects.get(pk=id)
        except Usuario2.DoesNotExist:
            return None
    
    def usuario2Crear(id, nombre, clave):
        usuario2 = Negocio.get_Usuario2(int(id))
        if (usuario2== None):
            usuario2 =  Usuario2(id, nombre, clave)
        else:
            usuario2.nombre = nombre
            usuario2.clave = clave
        usuario2.save()
        return True

    def usuario2Get(id):
        return Negocio.get_viewUsuario2(id)
    
    def usuario2Eliminar(id):
        usuario2 = Negocio.get_Usuario2(int(id))

        usuario2.delete()