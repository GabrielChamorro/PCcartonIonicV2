import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { CrudProductosPageRoutingModule } from './crud-productos-routing.module';

import { CrudProductosPage } from './crud-productos.page';
import { ReactiveFormsModule } from '@angular/forms'
@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    CrudProductosPageRoutingModule,
    ReactiveFormsModule
  ],
  declarations: [CrudProductosPage]
})
export class CrudProductosPageModule {}
