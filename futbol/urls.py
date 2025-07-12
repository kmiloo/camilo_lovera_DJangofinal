from django.urls import path
from . import views, api_views

urlpatterns = [
    # FBV CRUD
    path('jugadores/', views.listar_jugadores, name='listar_jugadores'),
    path('jugadores/crear/', views.crear_jugador, name='crear_jugador'),
    path('jugadores/editar/<int:id>/', views.editar_jugador, name='editar_jugador'),
    path('jugadores/eliminar/<int:id>/', views.eliminar_jugador, name='eliminar_jugador'),
    path('equipos/', views.listar_equipos, name='listar_equipos'),
    path('equipos/crear/', views.crear_equipo, name='crear_equipo'),
    path('equipos/editar/<int:id>/', views.editar_equipo, name='editar_equipo'),
    path('equipos/eliminar/<int:id>/', views.eliminar_equipo, name='eliminar_equipo'),

    # API endpoints
    path('api/jugadores/', api_views.api_jugadores),
    path('api/equipos/', api_views.api_equipos),
    path('api/torneos/', api_views.api_torneos),
    path('api/partidos/', api_views.api_partidos),
    path('api/paises/<int:id>/', api_views.api_pais_detalle),
    path('api/jugadores/<int:id>/', api_views.api_jugador_detalle),
    path('api/equipos/<int:id>/', api_views.api_equipo_detalle),
]
