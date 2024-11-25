import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PaginaPagarPage } from './pagina-pagar.page';

const routes: Routes = [
  {
    path: '',
    component: PaginaPagarPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PaginaPagarPageRoutingModule {}
