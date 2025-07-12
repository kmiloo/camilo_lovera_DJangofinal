from django.shortcuts import render, redirect, get_object_or_404
from .models import Jugador, Equipo
from .forms import JugadorForm, EquipoForm

# Jugadores
def listar_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'futbol/jugadores/listar.html', {'jugadores': jugadores})

def crear_jugador(request):
    form = JugadorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_jugadores')
    return render(request, 'futbol/jugadores/formulario.html', {'form': form})

def editar_jugador(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    form = JugadorForm(request.POST or None, request.FILES or None, instance=jugador)
    if form.is_valid():
        form.save()
        return redirect('listar_jugadores')
    return render(request, 'futbol/jugadores/formulario.html', {'form': form})

def eliminar_jugador(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    jugador.delete()
    return redirect('listar_jugadores')

# Equipos
def listar_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'futbol/equipos/listar.html', {'equipos': equipos})

def crear_equipo(request):
    form = EquipoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_equipos')
    return render(request, 'futbol/equipos/formulario.html', {'form': form})

def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    form = EquipoForm(request.POST or None, request.FILES or None, instance=equipo)
    if form.is_valid():
        form.save()
        return redirect('listar_equipos')
    return render(request, 'futbol/equipos/formulario.html', {'form': form})

def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    equipo.delete()
    return redirect('listar_equipos')
