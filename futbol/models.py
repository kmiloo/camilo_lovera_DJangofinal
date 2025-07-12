from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    entrenador = models.CharField(max_length=100)
    escudo = models.ImageField(upload_to='escudos/')

    def __str__(self):
        return self.nombre

class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class EquipoTorneo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='jugadores/')

    def __str__(self):
        return self.nombre

class Partido(models.Model):
    fecha = models.DateField()
    equipo_local = models.ForeignKey(Equipo, related_name='local', on_delete=models.CASCADE)
    equipo_visitante = models.ForeignKey(Equipo, related_name='visitante', on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()
