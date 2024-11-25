import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { PaginaPagarPageRoutingModule } from './pagina-pagar-routing.module';

import { PaginaPagarPage } from './pagina-pagar.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    PaginaPagarPageRoutingModule
  ],
  declarations: [PaginaPagarPage]
})
export class PaginaPagarPageModule {}
