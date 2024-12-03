import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { PaginaInicioPageRoutingModule } from './pagina-inicio-routing.module';

import { PaginaInicioPage } from './pagina-inicio.page';


@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    PaginaInicioPageRoutingModule,
    ReactiveFormsModule,
    
  ],
  declarations: [PaginaInicioPage]
})
export class PaginaInicioPageModule {}
