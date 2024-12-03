import { ClienteFormato } from "./ICliente";
import {EmpleadoFormato} from "./IEmpleado";

export interface UsuarioLogueadoFormato{
    nombre: string;
    idCliente?: ClienteFormato | null;
    idEmpleado?: EmpleadoFormato | null;
    'access_token': string,
    'refresh_token': string,
}