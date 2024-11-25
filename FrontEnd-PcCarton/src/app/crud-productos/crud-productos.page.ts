import { Component, OnInit } from '@angular/core';
import { ApiProductosService } from './../servicio/api-productos.service'
import { RespuestaApiProducto } from './../interfaces/RespuestaApiProducto'
import { ViewWillEnter, ViewWillLeave } from '@ionic/angular';
import { Subscription } from 'rxjs';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MenuController } from '@ionic/angular';  

@Component({
  selector: 'app-crud-productos',
  templateUrl: './crud-productos.page.html',
  styleUrls: ['./crud-productos.page.scss'],
})
export class CrudProductosPage implements ViewWillEnter, ViewWillLeave, OnInit {
  private suscripcionProducto!: Subscription;
  //public datos!: RespuestaApiProducto;
  //como tenia el profesor originalmente causaba error ya que faltaba inicialisar la variable en caso de que no encontrara nada.
  //como recomendacion se deberia dar una inicialisar siempre variables de este tipo para evitar errores a futuro
  public datos: RespuestaApiProducto = { OK: false, count: 0, msg: '', registro: [] };

  public formularioPost: FormGroup;

  constructor(
    public producto: ApiProductosService,
    private fb: FormBuilder,
    private menuController: MenuController
  ) {
    
    this.formularioPost = fb.group({
      descripVar: ["",[Validators.required, Validators.minLength(1)]],
      imagenPriVar: ["",[Validators.required, Validators.minLength(1)]], 
      idVar: [0,[Validators.required, Validators.minLength(1), Validators.min(0)]], 
      idCategVar: [0,[Validators.required, Validators.minLength(1), Validators.min(0)]],
      nombreVar: ["",[Validators.required, Validators.minLength(1)]], 
      precioVar: [0,[Validators.required, Validators.minLength(1), Validators.min(0)]], 
      stockVar: [0,[Validators.required, Validators.minLength(1), Validators.min(0)]]
    })
  }

  openAddProductMenu() {
    this.menuController.open('menuAddProduct');
  }

  public obtenerDatosPostProducto(){
    const esValido = this.formularioPost.valid;

    if(!esValido){
      alert("formularioPost es valido")
      return

    }
    
    const descripVar = this.formularioPost.getRawValue()?.descripVar;
    const imagenPriVar = this.formularioPost.getRawValue()?.imagenPriVar;
    const idVar = this.formularioPost.getRawValue()?.idVar;
    const idCategVar = this.formularioPost.getRawValue()?.idCategVar;
    const nombreVar = this.formularioPost.getRawValue()?.nombreVar;
    const precioVar = this.formularioPost.getRawValue()?.precioVar;
    const stockVar = this.formularioPost.getRawValue()?.stockVar;

    this.producto.postearProductos(descripVar,imagenPriVar,idVar,idCategVar,nombreVar,precioVar,stockVar);
    
    
    console.log("Valido:",this.formularioPost.valid);
    console.log("descripcion:",idCategVar);
    console.log("url imagen:",imagenPriVar)
    console.log("id:",idVar);
    console.log("nombre:",nombreVar);
    console.log("precio:",precioVar);
    console.log("stock",stockVar)
    this.producto.obtenerProductosSinDelay()

    
  }

  public obtenerDatosDeleteProducto(idProducto:any){
    
    this.producto.EliminarProductos(idProducto)
    this.producto.obtenerProductosSinDelay()

  }


  ionViewWillEnter(): void {
    this.suscripcionProducto = this.producto.productos.subscribe(losDatos => {
      if(losDatos){
        this.datos = losDatos;
      }
    }); 
    this.producto.obtenerProductosSinDelay()
  }

  ionViewWillLeave(): void {
    this.suscripcionProducto.unsubscribe();
    
  }

  ngOnInit() {
    
  }

}
