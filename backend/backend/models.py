#----Jesus Portales----

from django.db import models

class Comuna(models.Model):
    idComuna = models.IntegerField(primary_key=True, db_column='id_comuna')
    nombre = models.CharField(max_length=100)

    class Meta:
    	db_table = 'pp_comuna'

class Sedes(models.Model):
    idSede = models.IntegerField(primary_key=True, db_column='id_sede')
    direccion = models.CharField(max_length=100)
    cant_pisos = models.IntegerField(blank=True, null=True)  
    cant_salas = models.IntegerField(blank=True, null=True)  
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, db_column='id_comuna')


    class Meta:
    	db_table = 'pp_sedes'

