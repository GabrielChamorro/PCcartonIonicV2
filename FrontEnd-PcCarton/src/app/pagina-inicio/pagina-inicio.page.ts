import { Component, OnInit } from '@angular/core';
import { ApiProductosService } from './../servicio/api-productos.service';
import { RespuestaApiProducto } from './../interfaces/RespuestaApiProducto';
import { ViewWillEnter, ViewWillLeave } from '@ionic/angular';
import { Subscription } from 'rxjs';
import { Router } from '@angular/router';
import { WebpayService } from './../servicio/webpay.service';

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
    private router: Router,
    private webpayService: WebpayService
  ) { }

  public redirigirLogin() {
    this.router.navigate(['/','login']);
  }

  public buscar() {
    // Lógica para la búsqueda
  }

  public realizarPago() {
    const data = {
      buy_order: 'ordenCompra12345678',
      session_id: 'sesion1234557545',
      amount: 10000,
      return_url: 'http://www.comercio.cl/webpay/retorno'
    };

    this.webpayService.iniciarTransaccion(data).subscribe(response => {
      console.log('Pago iniciado:', response);
      if (response.token && response.url) {
        // Redirige al usuario a la URL de pago proporcionada por Webpay con el token
        window.location.href = `${response.url}?token_ws=${response.token}`;
      } else {
        console.error('Error en la respuesta de Webpay:', response);
      }
    }, error => {
      console.error('Error al iniciar la transacción:', error);
    });
  }


  public confirmarTransaccion(token: string) {
    this.webpayService.confirmarTransaccion(token).subscribe(response => {
      console.log('Transacción confirmada:', response);
      // Maneja la confirmación de la transacción aquí
    }, error => {
      console.error('Error al confirmar la transacción:', error);
    });
  }
  

  ionViewWillEnter(): void {
    this.suscripcionProducto = this.producto.productos.subscribe(losDatos => {
      if (losDatos) {
        this.datos = losDatos;
      }
    });
    this.producto.obtenerProductos();
  }

  ionViewWillLeave(): void {
    this.suscripcionProducto.unsubscribe();
  }

  ngOnInit() { }
}
