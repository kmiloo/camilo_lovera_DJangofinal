from rest_framework import serializers
from .models import *

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'

class EquipoSerializer(serializers.ModelSerializer):
    jugadores = JugadorSerializer(many=True, read_only=True, source='jugador_set')
    class Meta:
        model = Equipo
        fields = '__all__'

class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = '__all__'

class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = '__all__'

class PaisSerializer(serializers.ModelSerializer):
    equipos = EquipoSerializer(many=True, read_only=True, source='equipo_set')
    jugadores = JugadorSerializer(many=True, read_only=True, source='jugador_set')
    torneos = TorneoSerializer(many=True, read_only=True, source='torneo_set')
    class Meta:
        model = Pais
        fields = '__all__'
