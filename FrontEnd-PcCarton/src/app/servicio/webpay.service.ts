import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WebpayService {
  private apiUrl = 'http://localhost:9010/ventas/iniciar-transaccion/';
  private integracionUrl =  'https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions'

  constructor(private http: HttpClient) {}

  iniciarTransaccion(data: any): Observable<any> {
    return this.http.post(this.apiUrl, data);
  }

  public confirmarTransaccion(token: string): Observable<any> {
    return this.http.put(`${this.apiUrl}confirmar-transaccion/${token}`, {});
  }
  


  
}

