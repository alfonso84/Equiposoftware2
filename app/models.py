# -*- coding: utf-8 -*-
import math
from django.db import models


class Seleccion(models.Model):
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.pais

    class Meta:
        managed = True
        db_table = 'selecciones'


class Jugador(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.ForeignKey('Seleccion', on_delete=models.CASCADE)
    puntaje = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'jugadores'
