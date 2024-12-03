import { Component, OnInit } from '@angular/core';
import { ApiProductosService } from './../servicio/api-productos.service'
import { RespuestaApiProducto } from './../interfaces/RespuestaApiProducto'
import { ViewWillEnter, ViewWillLeave } from '@ionic/angular';
import { Subscription } from 'rxjs';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MenuController } from '@ionic/angular';
import { Router } from '@angular/router';



@Component({
  selector: 'app-pagina-inicio',
  templateUrl: './pagina-inicio.page.html',
  styleUrls: ['./pagina-inicio.page.scss'],
})
export class PaginaInicioPage implements ViewWillEnter, ViewWillLeave, OnInit {
  private suscripcionProducto!: Subscription;
  public datos: RespuestaApiProducto = { OK: false, count: 0, msg: '', registro: [] };
  constructor(
    public producto: ApiProductosService,
    private router: Router
  ) { }


  public redirigirLogin(){
    this.router.navigate(['/','login']);
  }

  public buscar(){
    
  }
  

  ionViewWillEnter(): void {
    this.suscripcionProducto = this.producto.productos.subscribe(losDatos => {
      if(losDatos){
        this.datos = losDatos;
      }
    }); 
    this.producto.obtenerProductos()
    
  }


  ionViewWillLeave(): void {
    this.suscripcionProducto.unsubscribe();
  }


  ngOnInit() {
  }


}
