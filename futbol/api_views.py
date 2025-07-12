from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])
def api_jugadores(request):
    return Response(JugadorSerializer(Jugador.objects.all(), many=True).data)

@api_view(['GET'])
def api_equipos(request):
    return Response(EquipoSerializer(Equipo.objects.all(), many=True).data)

@api_view(['GET'])
def api_torneos(request):
    return Response(TorneoSerializer(Torneo.objects.all(), many=True).data)

@api_view(['GET'])
def api_partidos(request):
    return Response(PartidoSerializer(Partido.objects.all(), many=True).data)

@api_view(['GET'])
def api_pais_detalle(request, id):
    pais = get_object_or_404(Pais, id=id)
    return Response(PaisSerializer(pais).data)

@api_view(['GET'])
def api_jugador_detalle(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    return Response(JugadorSerializer(jugador).data)

@api_view(['GET'])
def api_equipo_detalle(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    return Response(EquipoSerializer(equipo).data)
