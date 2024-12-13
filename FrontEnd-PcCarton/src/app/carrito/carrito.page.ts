import { Component } from '@angular/core';
import { AlertController, NavController } from '@ionic/angular';
import { WebpayService } from './../servicio/webpay.service'; // Importa el servicio de Webpay

@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.page.html',
  styleUrls: ['./carrito.page.scss'],
})
export class CarritoPage {
  carrito: any[] = [];

  constructor(
    private alertController: AlertController,
    private navCtrl: NavController,
    private webpayService: WebpayService // Inyecta el servicio de Webpay
  ) { }

  ionViewWillEnter() {
    const carritoGuardado = localStorage.getItem('carrito');
    this.carrito = carritoGuardado ? JSON.parse(carritoGuardado) : [];
  }

  aumentarCantidad(indice: number) {
    this.carrito[indice].cantidad++;
    this.actualizarLocalStorage();
  }

  disminuirCantidad(indice: number) {
    if (this.carrito[indice].cantidad > 1) {
      this.carrito[indice].cantidad--;
    } else {
      this.eliminarProducto(indice);
    }
    this.actualizarLocalStorage();
  }

  eliminarProducto(indice: number) {
    this.carrito.splice(indice, 1);
    this.actualizarLocalStorage();
  }

  obtenerPrecioTotal() {
    return this.carrito.reduce((acumulador, producto) => acumulador + producto.precio * producto.cantidad, 0);
  }

  async realizarCompra() {
    const total = this.obtenerPrecioTotal();
    const buyOrder = this.generarIdCompraAleatoria();

    const alerta = await this.alertController.create({
      header: 'Confirmación',
      message: `El total de su compra es de $${total}. ¿Desea continuar?`,
      buttons: [
        {
          text: 'Cancelar',
          role: 'cancel',
          cssClass: 'secondary',
        },
        {
          text: 'Aceptar',
          handler: () => {
            this.procesarPago(buyOrder, total);
          },
        },
      ],
    });

    await alerta.present();
  }

  generarIdCompraAleatoria() {
    return 'ordenCompra' + Math.floor(Math.random() * 100000000);
  }

  procesarPago(buyOrder: string, amount: number) {
    const data = {
      buy_order: buyOrder,
      session_id: 'sesion' + Math.floor(Math.random() * 100000000),
      amount: amount,
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

  actualizarLocalStorage() {
    localStorage.setItem('carrito', JSON.stringify(this.carrito));
  }
}
