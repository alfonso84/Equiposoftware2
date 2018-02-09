# -*- coding: utf-8 -*-
from django.urls import path

from . import ajax
from . import views


urlpatterns = [
    path('', views.EquipoView.as_view(), name='equipo'),
    path('ajax/obtener_jugadores', ajax.obtener_jugadores, name='ajax_obtener_jugadores'),
]
