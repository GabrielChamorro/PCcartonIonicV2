import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import {RespuestaApiProducto} from './../interfaces/RespuestaApiProducto'
import { BehaviorSubject, delay } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ApiProductosService {
  private readonly URL_PostProducto = "http://localhost:9010/ventas/backend/producto/";
  private $productos = new BehaviorSubject<RespuestaApiProducto | null>(null);
  public productos = this.$productos.asObservable();
  private $cargando = new BehaviorSubject<boolean>(false);
  public cargando = this.$cargando.asObservable();
  public usuarioActivo: RespuestaApiProducto | null = null;

  constructor(
    private http: HttpClient
  ) { }

  obtenerProductos(){
    this.$cargando.next(true);
    this.http.get<RespuestaApiProducto>("http://localhost:9010/ventas/backend/producto/")
    .pipe(delay(1000))
    .subscribe(losDatos =>{
      this.$productos.next(losDatos);
      this.$cargando.next(false);
      console.log("los datos de la api son");
      console.log(losDatos)
    })
  }

  obtenerProductosSinDelay(){
    this.$cargando.next(true);
    this.http.get<RespuestaApiProducto>("http://localhost:9010/ventas/backend/producto/")
    .subscribe(losDatos =>{
      this.$productos.next(losDatos);
      this.$cargando.next(false);
      console.log("los datos de la api son");
      console.log(losDatos)
    })
  }



  /*
  Ingreso primero las variables que va a usar el post.

  Armo el "cuerpo" donde van a ir las variables

  armo la solicitud post la cual es en formato "RespuestaApiProducto" aunque puede que tenga que ser con Producto
  */
  postearProductos(descripVar: string, imagenPriVar: string, idVar: number, idCategVar: number, nombreVar: string, precioVar: number, stockVar: number){
    const cuerpo = {
      descripcion: descripVar,
      imagenPrincipal: imagenPriVar, 
      id: idVar, 
      idCategoria: idCategVar, 
      nombre: nombreVar, 
      precio: precioVar, 
      stock: stockVar
    }
    
    //aqui mando el post para enviar los datos 

    this.http.post<RespuestaApiProducto>(
      this.URL_PostProducto,
      JSON.stringify(cuerpo),
      {
        headers:{
          "Content-type": "application/json"
        }
      }
    )
    
    //la subscripcion es OBLIGATORIA para todos los metodos, es un copypaste nomas
    .subscribe( datos => {
      console.log(datos); 
    });

    this.obtenerProductos()
    
  }

  putearProductos(descripVar: string, idVar: number, idCategVar: number, nombreVar: string, precioVar: number, stockVar: number){
    const cuerpo = {
      descripcion: descripVar, 
      id: idVar, 
      idCategoria: idCategVar, 
      nombre: nombreVar, 
      precio: precioVar, 
      stock: stockVar
    }
    
    //aqui mando el post para enviar los datos 

    this.http.put<RespuestaApiProducto>(
      this.URL_PostProducto,
      JSON.stringify(cuerpo),
      {
        headers:{
          "Content-type": "application/json"
        }
      }
    )

    //la subscripcion es OBLIGATORIA para todos los metodos, es un copypaste nomas
    .subscribe( datos => {
      console.log(datos);
    });
  }

  EliminarProductos(ValorId: number){
    

    this.http.delete<RespuestaApiProducto>(
      this.URL_PostProducto+ValorId,
    )

    
    //la subscripcion es OBLIGATORIA para todos los metodos, es un copypaste nomas
    .subscribe( datos => {
      console.log(datos);
    });

    
  }

}
