from .models import *


class Negocio:

    #courrier
    def get_Courrier(id):
        try:
            return Courrier.objects.get(pk=id)
        except Courrier.DoesNotExist:
            return None

    def courrierCrear(id, precioKM, descripcion, telefono, rut):
        courrier = Negocio.get_Courrier(id)
        if courrier is None:
            courrier = Courrier(id=id, precioKM=precioKM, descripcion=descripcion, telefono=telefono, rut=rut)
        else:
            courrier.precioKM = precioKM
            courrier.descripcion = descripcion
            courrier.telefono = telefono
            courrier.rut = rut
        courrier.save()
        return True

    def courrierEliminar(id):
        courrier = Negocio.get_Courrier(id)
        if courrier:
            courrier.delete()
            return True
        else:
            raise ValueError("El Courrier con el ID especificado no existe")
        
    #MedioDePago

    def get_MedioDePago(id):
        try:
            return MedioDePago.objects.get(pk=id)
        except MedioDePago.DoesNotExist:
            return None

    def medioDePagoCrear(id, nombre, descripcion):
        medioDePago = Negocio.get_MedioDePago(id)
        if medioDePago is None:
            medioDePago = MedioDePago(id=id, nombre=nombre, descripcion=descripcion)
        else:
            medioDePago.nombre = nombre
            medioDePago.descripcion = descripcion
        medioDePago.save()
        return True

    def medioDePagoEliminar(id):
        medioDePago = Negocio.get_MedioDePago(id)
        if medioDePago:
            medioDePago.delete()
            return True
        else:
            raise ValueError("El Medio de Pago con el ID especificado no existe")


    #Factura

    def get_Factura(id):
        try:
            return Factura.objects.get(pk=id)
        except Factura.DoesNotExist:
            return None

    def facturaCrear(id, numeroFactura, fecha, descripcion, idCourrier, idPago, total):
        factura = Negocio.get_Factura(id)
        try:
            courrier = Courrier.objects.get(pk=idCourrier)
            medioDePago = MedioDePago.objects.get(pk=idPago)
        except (Courrier.DoesNotExist, MedioDePago.DoesNotExist):
            raise ValueError("Courrier o Medio de Pago no válido")

        if factura is None:
            factura = Factura(id=id, numeroFactura=numeroFactura, fecha=fecha, descripcion=descripcion,
                            idCourrier=courrier, idPago=medioDePago, total=total)
        else:
            factura.numeroFactura = numeroFactura
            factura.fecha = fecha
            factura.descripcion = descripcion
            factura.idCourrier = courrier
            factura.idPago = medioDePago
            factura.total = total
        factura.save()
        return True

    def facturaEliminar(id):
        factura = Negocio.get_Factura(id)
        if factura:
            factura.delete()
            return True
        else:
            raise ValueError("La Factura con el ID especificado no existe")
        
    
    #TipoEnvio

    def get_TipoDeEnvio(id):
        try:
            return TipoDeEnvio.objects.get(pk=id)
        except TipoDeEnvio.DoesNotExist:
            return None

    def tipoDeEnvioCrear(id, nombre, descripcion):
        tipoDeEnvio = Negocio.get_TipoDeEnvio(id)
        if tipoDeEnvio is None:
            tipoDeEnvio = TipoDeEnvio(id=id, nombre=nombre, descripcion=descripcion)
        else:
            tipoDeEnvio.nombre = nombre
            tipoDeEnvio.descripcion = descripcion
        tipoDeEnvio.save()
        return True

    def tipoDeEnvioEliminar(id):
        tipoDeEnvio = Negocio.get_TipoDeEnvio(id)
        if tipoDeEnvio:
            tipoDeEnvio.delete()
            return True
        else:
            raise ValueError("El Tipo de Envío con el ID especificado no existe")


    #Region

    def get_Region(id):
        try:
            return Region.objects.get(pk=id)
        except Region.DoesNotExist:
            return None

    def regionCrear(id, nombre):
        region = Negocio.get_Region(id)
        if region is None:
            region = Region(id=id, nombre=nombre)
        else:
            region.nombre = nombre
        region.save()
        return True

    def regionEliminar(id):
        region = Negocio.get_Region(id)
        if region:
            region.delete()
            return True
        else:
            raise ValueError("La Región con el ID especificado no existe")
        
    #Ciudad

    def get_Ciudad(id):
        try:
            return Ciudad.objects.get(pk=id)
        except Ciudad.DoesNotExist:
            return None

    def ciudadCrear(id, nombre, idRegion):
        try:
            region = Region.objects.get(pk=idRegion)
        except Region.DoesNotExist:
            raise ValueError("La Región especificada no existe")

        ciudad = Negocio.get_Ciudad(id)
        if ciudad is None:
            ciudad = Ciudad(id=id, nombre=nombre, idRegion=region)
        else:
            ciudad.nombre = nombre
            ciudad.idRegion = region
        ciudad.save()
        return True

    def ciudadEliminar(id):
        ciudad = Negocio.get_Ciudad(id)
        if ciudad:
            ciudad.delete()
            return True
        else:
            raise ValueError("La Ciudad con el ID especificado no existe")
        
    
    #Comuna


    def get_Comuna(id):
        try:
            return Comuna.objects.get(pk=id)
        except Comuna.DoesNotExist:
            return None

    def comunaCrear(id, nombre, idCiudad):
        try:
            ciudad = Ciudad.objects.get(pk=idCiudad)
        except Ciudad.DoesNotExist:
            raise ValueError("La Ciudad especificada no existe")

        comuna = Negocio.get_Comuna(id)
        if comuna is None:
            comuna = Comuna(id=id, nombre=nombre, idCiudad=ciudad)
        else:
            comuna.nombre = nombre
            comuna.idCiudad = ciudad
        comuna.save()
        return True

    def comunaEliminar(id):
        comuna = Negocio.get_Comuna(id)
        if comuna:
            comuna.delete()
            return True
        else:
            raise ValueError("La Comuna con el ID especificado no existe")
        
    
    #Direccion

    def get_Direccion(id):
        try:
            return Direccion.objects.get(pk=id)
        except Direccion.DoesNotExist:
            return None

    def direccionCrear(id, nombre, direccion, numero, depto, idComuna):
        try:
            comuna = Comuna.objects.get(pk=idComuna)
        except Comuna.DoesNotExist:
            raise ValueError("La Comuna especificada no existe")

        direccion_obj = Negocio.get_Direccion(id)
        if direccion_obj is None:
            direccion_obj = Direccion(id=id, nombre=nombre, direccion=direccion, numero=numero, depto=depto, idComuna=comuna)
        else:
            direccion_obj.nombre = nombre
            direccion_obj.direccion = direccion
            direccion_obj.numero = numero
            direccion_obj.depto = depto
            direccion_obj.idComuna = comuna
        direccion_obj.save()
        return True

    def direccionEliminar(id):
        direccion_obj = Negocio.get_Direccion(id)
        if direccion_obj:
            direccion_obj.delete()
            return True
        else:
            raise ValueError("La Dirección con el ID especificado no existe")


    #Categoria


    def get_Categoria(id):
        try:
            return Categoria.objects.get(pk=id)
        except Categoria.DoesNotExist:
            return None

    def categoriaCrear(id, nombre, descripcion, idPadre=None):
        idPadre_obj = None
        if idPadre:
            idPadre_obj = Negocio.get_Categoria(idPadre)
            if idPadre_obj is None:
                raise ValueError("La Categoría padre especificada no existe")

        categoria = Negocio.get_Categoria(id)
        if categoria is None:
            categoria = Categoria(id=id, nombre=nombre, descripcion=descripcion, idPadre=idPadre_obj)
        else:
            categoria.nombre = nombre
            categoria.descripcion = descripcion
            categoria.idPadre = idPadre_obj
        categoria.save()
        return True

    def categoriaEliminar(id):
        categoria = Negocio.get_Categoria(id)
        if categoria:
            categoria.delete()
            return True
        else:
            raise ValueError("La Categoría con el ID especificado no existe")
        

    #CategoriaEmpleado

    def get_CategoriaEmpleado(id):
        try:
            return CategoriaEmpleado.objects.get(pk=id)
        except CategoriaEmpleado.DoesNotExist:
            return None

    def categoriaEmpleadoCrear(id, nombre, descripcion, idPadre=None):
        idPadre_obj = None
        if idPadre:
            idPadre_obj = Negocio.get_CategoriaEmpleado(idPadre)
            if idPadre_obj is None:
                raise ValueError("La Categoría Empleado padre especificada no existe")

        categoriaEmpleado = Negocio.get_CategoriaEmpleado(id)
        if categoriaEmpleado is None:
            categoriaEmpleado = CategoriaEmpleado(id=id, nombre=nombre, descripcion=descripcion, idPadre=idPadre_obj)
        else:
            categoriaEmpleado.nombre = nombre
            categoriaEmpleado.descripcion = descripcion
            categoriaEmpleado.idPadre = idPadre_obj
        categoriaEmpleado.save()
        return True

    def categoriaEmpleadoEliminar(id):
        categoriaEmpleado = Negocio.get_CategoriaEmpleado(id)
        if categoriaEmpleado:
            categoriaEmpleado.delete()
            return True
        else:
            raise ValueError("La Categoría Empleado con el ID especificado no existe")

    #Sucursal

    def get_Sucursal(id):
        try:
            return Sucursal.objects.get(pk=id)
        except Sucursal.DoesNotExist:
            return None

    def sucursalCrear(id, nombre, descripcion, idDireccion):
        try:
            direccion = Direccion.objects.get(pk=idDireccion)
        except Direccion.DoesNotExist:
            raise ValueError("La Dirección especificada no existe")

        sucursal = Negocio.get_Sucursal(id)
        if sucursal is None:
            sucursal = Sucursal(id=id, nombre=nombre, descripcion=descripcion, direccion=direccion)
        else:
            sucursal.nombre = nombre
            sucursal.descripcion = descripcion
            sucursal.direccion = direccion
        sucursal.save()
        return True

    def sucursalEliminar(id):
        sucursal = Negocio.get_Sucursal(id)
        if sucursal:
            sucursal.delete()
            return True
        else:
            raise ValueError("La Sucursal con el ID especificado no existe")
        


    #Cliente

    def get_Cliente(id):
        try:
            return Cliente.objects.get(pk=id)
        except Cliente.DoesNotExist:
            return None

    def clienteCrear(id, nombre, telefono, mail, clave, idDireccion):
        try:
            direccion = Direccion.objects.get(pk=idDireccion)
        except Direccion.DoesNotExist:
            raise ValueError("La Dirección especificada no existe")

        cliente = Negocio.get_Cliente(id)
        if cliente is None:
            cliente = Cliente(id=id, nombre=nombre, telefono=telefono, mail=mail, clave=clave, direccion=direccion)
        else:
            cliente.nombre = nombre
            cliente.telefono = telefono
            cliente.mail = mail
            cliente.clave = clave
            cliente.direccion = direccion
        cliente.save()
        return True

    def clienteEliminar(id):
        cliente = Negocio.  get_Cliente(id)
        if cliente:
            cliente.delete()
            return True
        else:
            raise ValueError("El Cliente con el ID especificado no existe")


    #Empleado

    def get_Empleado(id):
        try:
            return Empleado.objects.get(pk=id)
        except Empleado.DoesNotExist:
            return None

    def empleadoCrear(id, nombre, idCategoria):
        try:
            categoria = Categoria.objects.get(pk=idCategoria)
        except Categoria.DoesNotExist:
            raise ValueError("La Categoría especificada no existe")

        empleado = Negocio.get_Empleado(id)
        if empleado is None:
            empleado = Empleado(id=id, nombre=nombre, idCategoria=categoria)
        else:
            empleado.nombre = nombre
            empleado.idCategoria = categoria
        empleado.save()
        return True

    def empleadoEliminar(id):
        empleado = Negocio.get_Empleado(id)
        if empleado:
            empleado.delete()
            return True
        else:
            raise ValueError("El Empleado con el ID especificado no existe")
        

    #Usuario

    def get_Usuario(nombre):
        try:
            return Usuario.objects.get(pk=nombre)
        except Usuario.DoesNotExist:
            return None

    def usuarioCrear(nombre, clave,idCliente=None, idEmpleado=None):
        cliente = None
        empleado = None

        if idCliente:
            try:
                cliente = Cliente.objects.get(pk=idCliente)
            except Cliente.DoesNotExist:
                raise ValueError("El Cliente especificado no existe")

        if idEmpleado:
            try:
                empleado = Empleado.objects.get(pk=idEmpleado)
            except Empleado.DoesNotExist:
                raise ValueError("El Empleado especificado no existe")

        usuario = Negocio.get_Usuario(nombre)
        if usuario is None:
            usuario = Usuario(nombre=nombre,clave=clave, idCliente=cliente, idEmpleado=empleado)
        else:
            usuario.clave = clave
            usuario.idCliente = cliente
            usuario.idEmpleado = empleado
        usuario.save()
        return True

    def usuarioEliminar(nombre):
        usuario = Negocio.get_Usuario(nombre)
        if usuario:
            usuario.delete()
            return True
        else:
            raise ValueError("El Usuario con el ID especificado no existe")
        


    #Boleta

    def get_Boleta(id):
        try:
            return Boleta.objects.get(pk=id)
        except Boleta.DoesNotExist:
            return None

    def boletaCrear(id, numeroBoleta, fecha, descripcion, idCliente, idEmpleado, idPago, total):
        try:
            cliente = Cliente.objects.get(pk=idCliente)
            empleado = Empleado.objects.get(pk=idEmpleado)
            pago = MedioDePago.objects.get(pk=idPago)
        except (Cliente.DoesNotExist, Empleado.DoesNotExist, MedioDePago.DoesNotExist) as e:
            raise ValueError("Un Cliente, Empleado o Medio de Pago especificado no existe")

        boleta = Negocio.get_Boleta(id)
        if boleta is None:
            boleta = Boleta(
                id=id,
                numeroBoleta=numeroBoleta,
                fecha=fecha,
                descripcion=descripcion,
                idCliente=cliente,
                idEmpleado=empleado,
                idPago=pago,
                total=total
            )
        else:
            boleta.numeroBoleta = numeroBoleta
            boleta.fecha = fecha
            boleta.descripcion = descripcion
            boleta.idCliente = cliente
            boleta.idEmpleado = empleado
            boleta.idPago = pago
            boleta.total = total
        boleta.save()
        return True

    def boletaEliminar(id):
        boleta = Negocio.get_Boleta(id)
        if boleta:
            boleta.delete()
            return True
        else:
            raise ValueError("La Boleta con el ID especificado no existe")


    #BoletaDetalle


    def get_BoletaDetalle(id):
        try:
            return BoletaDetalle.objects.get(pk=id)
        except BoletaDetalle.DoesNotExist:
            return None

    def boletaDetalleCrear(id, fecha, descripcion, idProducto, idEnvio, idBoleta, total, cantidad, precio):
        try:
            producto = Producto.objects.get(pk=idProducto)
            envio = TipoDeEnvio.objects.get(pk=idEnvio)
            boleta = Boleta.objects.get(pk=idBoleta)
        except (Producto.DoesNotExist, TipoDeEnvio.DoesNotExist, Boleta.DoesNotExist) as e:
            raise ValueError("El Producto, Tipo de Envío o Boleta especificado no existe")

        boleta_detalle = Negocio.get_BoletaDetalle(id)
        if boleta_detalle is None:
            boleta_detalle = BoletaDetalle(
                id=id,
                fecha=fecha,
                descripcion=descripcion,
                idProducto=producto,
                idEnvio=envio,
                idBoleta=boleta,
                total=total,
                cantidad=cantidad,
                precio=precio
            )
        else:
            boleta_detalle.fecha = fecha
            boleta_detalle.descripcion = descripcion
            boleta_detalle.idProducto = producto
            boleta_detalle.idEnvio = envio
            boleta_detalle.idBoleta = boleta
            boleta_detalle.total = total
            boleta_detalle.cantidad = cantidad
            boleta_detalle.precio = precio
        boleta_detalle.save()
        return True

    def boletaDetalleEliminar(id):
        boleta_detalle = Negocio.get_BoletaDetalle(id)
        if boleta_detalle:
            boleta_detalle.delete()
            return True
        else:
            raise ValueError("El Detalle de Boleta con el ID especificado no existe")


    #Compra

    def get_Compra(id):
        try:
            return Compra.objects.get(pk=id)
        except Compra.DoesNotExist:
            return None

    def compraCrear(id, numeroBoleta, fecha, descripcion, idCliente, idEmpleado, idPago, idCourrier, total):
        try:
            cliente = Cliente.objects.get(pk=idCliente)
            empleado = Empleado.objects.get(pk=idEmpleado)
            pago = MedioDePago.objects.get(pk=idPago)
            courrier = Courrier.objects.get(pk=idCourrier)
        except (Cliente.DoesNotExist, Empleado.DoesNotExist, MedioDePago.DoesNotExist, Courrier.DoesNotExist) as e:
            raise ValueError("Un Cliente, Empleado, Medio de Pago o Courrier especificado no existe")

        compra = Negocio.get_Compra(id)
        if compra is None:
            compra = Compra(
                id=id,
                numeroBoleta=numeroBoleta,
                fecha=fecha,
                descripcion=descripcion,
                idCliente=cliente,
                idEmpleado=empleado,
                idPago=pago,
                idCourrier=courrier,
                total=total
            )
        else:
            compra.numeroBoleta = numeroBoleta
            compra.fecha = fecha
            compra.descripcion = descripcion
            compra.idCliente = cliente
            compra.idEmpleado = empleado
            compra.idPago = pago
            compra.idCourrier = courrier
            compra.total = total
        compra.save()
        return True

    def compraEliminar(id):
        compra = Negocio.get_Compra(id)
        if compra:
            compra.delete()
            return True
        else:
            raise ValueError("La Compra con el ID especificado no existe")


    #CompraDetalle


    def get_CompraDetalle(id):
        try:
            return CompraDetalle.objects.get(pk=id)
        except CompraDetalle.DoesNotExist:
            return None

    def compraDetalleCrear(id, fecha, descripcion, idProducto, idEnvio, idCompra, total, cantidad, precio):
        try:
            producto = Producto.objects.get(pk=idProducto)
            envio = TipoDeEnvio.objects.get(pk=idEnvio)
            compra = Compra.objects.get(pk=idCompra)
        except (Producto.DoesNotExist, TipoDeEnvio.DoesNotExist, Compra.DoesNotExist) as e:
            raise ValueError("El Producto, Tipo de Envío o Compra especificado no existe")

        compra_detalle = Negocio.get_CompraDetalle(id)
        if compra_detalle is None:
            compra_detalle = CompraDetalle(
                id=id,
                fecha=fecha,
                descripcion=descripcion,
                idProducto=producto,
                idEnvio=envio,
                idCompra=compra,
                total=total,
                cantidad=cantidad,
                precio=precio
            )
        else:
            compra_detalle.fecha = fecha
            compra_detalle.descripcion = descripcion
            compra_detalle.idProducto = producto
            compra_detalle.idEnvio = envio
            compra_detalle.idCompra = compra
            compra_detalle.total = total
            compra_detalle.cantidad = cantidad
            compra_detalle.precio = precio
        compra_detalle.save()
        return True

    def compraDetalleEliminar(id):
        compra_detalle = Negocio.get_CompraDetalle(id)
        if compra_detalle:
            compra_detalle.delete()
            return True
        else:
            raise ValueError("El Detalle de Compra con el ID especificado no existe")

    #CompraCarrito

    def get_CompraCarrito(id):
        try:
            return CompraCarrito.objects.get(pk=id)
        except CompraCarrito.DoesNotExist:
            return None

    def compraCarritoCrear(id, fecha, descripcion, idProducto, idEnvio, total, cantidad, precio):
        try:
            producto = Producto.objects.get(pk=idProducto)
            envio = TipoDeEnvio.objects.get(pk=idEnvio)
        except (Producto.DoesNotExist, TipoDeEnvio.DoesNotExist) as e:
            raise ValueError("El Producto o Tipo de Envío especificado no existe")

        compra_carrito = Negocio.get_CompraCarrito(id)
        if compra_carrito is None:
            compra_carrito = CompraCarrito(
                id=id,
                fecha=fecha,
                descripcion=descripcion,
                idProducto=producto,
                idEnvio=envio,
                total=total,
                cantidad=cantidad,
                precio=precio
            )
        else:
            compra_carrito.fecha = fecha
            compra_carrito.descripcion = descripcion
            compra_carrito.idProducto = producto
            compra_carrito.idEnvio = envio
            compra_carrito.total = total
            compra_carrito.cantidad = cantidad
            compra_carrito.precio = precio
        compra_carrito.save()
        return True

    def compraCarritoEliminar(id):
        compra_carrito = Negocio.get_CompraCarrito(id)
        if compra_carrito:
            compra_carrito.delete()
            return True
        else:
            raise ValueError("El Carrito de Compra con el ID especificado no existe")
        
    #



    #Producto
    
    def get_Producto(id):
        try:
            return Producto.objects.get(pk=id)
        except Producto.DoesNotExist:
            return None 
    
    def productoCrear(id, nombre, descripcion, imagenPrincipal, precio, stock, idCategoria):
        producto = Negocio.get_Producto(int(id))
        if (producto== None):
            try:
                precio = int(precio)
                if precio > 25:
                    producto = Producto(id, nombre, descripcion, imagenPrincipal, precio, stock, idCategoria)
                else:
                    raise ValueError("El precio debe ser mayor a 25")
            except ValueError:
                raise ValueError("El precio debe ser un numero")
        else:
            producto.nombre = nombre
            producto.descripcion = descripcion
            producto.imagenPrincipal = imagenPrincipal
            producto.precio = precio
            producto.stock = stock
            clCategoria = Categoria(idCategoria)
            producto.idCategoria = clCategoria
        print("producto", producto)
        producto.save()
        return True


    def productoGet(id):
        return Negocio.get_Producto(id)
    
    def productoEliminar(id):
        producto = Negocio.get_Producto(int(id))
        producto.delete() 

