# -*- coding: utf-8 -*-
from django.http import JsonResponse

from .models import Jugador, Seleccion


def obtener_jugadores(request):
    pais_id = request.GET.get('pais_id')
    jugadores_select = '<option value="" selected="selected">---------</option>'
    if pais_id:
        pais = Seleccion.objects.get(pk=pais_id)
        jugadores = Jugador.objects.filter(pais=pais).order_by('nombre')
        for jugador in jugadores:
            jugadores_select += '<option value="%s">%s</option>' % (
                jugador.id,
                jugador.nombre
            )
    response = {}
    response['jugadores'] = jugadores_select
    return JsonResponse(response)
