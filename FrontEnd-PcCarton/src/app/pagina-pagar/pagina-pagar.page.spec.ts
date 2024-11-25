import { ComponentFixture, TestBed } from '@angular/core/testing';
import { PaginaPagarPage } from './pagina-pagar.page';

describe('PaginaPagarPage', () => {
  let component: PaginaPagarPage;
  let fixture: ComponentFixture<PaginaPagarPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(PaginaPagarPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
