import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CuerpoLogin } from './../interfaces/CuerpoLogin'; //el formato de los datos con los que hago login
import { UsuarioLogueadoFormato } from './../interfaces/IUsuario'; //el formato de los datos que recibo al enviar el token
import { BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private readonly URL_LOGIN: string = 'http://localhost:9010/ventas/backend/login/';
  public UsuarioLogueadoFormato: UsuarioLogueadoFormato | null = null;
  public accessToken: string | null = null;
  // Observador de cargando
  private $cargando = new BehaviorSubject<boolean>(false);
  public cargando = this.$cargando.asObservable();
  constructor(
    private http: HttpClient,
    private router: Router
  ) {

  }

  public iniciarSesion(usuarioVar: string, contraseniaVar: string){
    this.$cargando.next(true);

    const cuerpo: CuerpoLogin = {
      nombre: usuarioVar,
      clave: contraseniaVar
    }
    this.http.post<UsuarioLogueadoFormato>(this.URL_LOGIN, JSON.stringify(cuerpo), {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .subscribe(resultado  => {
      this.UsuarioLogueadoFormato = resultado;
      this.accessToken = resultado.access_token;
      this.$cargando.next(false);
      console.log(resultado);
      this.router.navigate(['/','pagina-inicio']);
    });

  }

  public cerrarSesion(){
    if(this.UsuarioLogueadoFormato){
      this.UsuarioLogueadoFormato = null;
      this.accessToken = null;
    }
  }
}
