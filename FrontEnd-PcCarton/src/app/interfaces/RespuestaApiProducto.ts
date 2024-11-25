import {Producto} from './Producto'
export interface RespuestaApiProducto {
    OK: boolean,
    count: number,
    msg: string,
    registro: Producto[]
}