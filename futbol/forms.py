from django import forms
from .models import Jugador, Equipo

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
