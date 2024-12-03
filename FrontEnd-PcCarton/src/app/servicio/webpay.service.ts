import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WebpayService {
  private apiUrl = 'https://webpay3g.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions';

  constructor(private http: HttpClient) {}

  iniciarTransaccion(data: any): Observable<any> {
    return this.http.post(this.apiUrl, data, {
      headers: {
        'Tbk-Api-Key-Id': 'TU_API_KEY',
        'Tbk-Api-Key-Secret': 'TU_SECRET_KEY',
        'Content-Type': 'application/json'
      }
    });
  }
}

