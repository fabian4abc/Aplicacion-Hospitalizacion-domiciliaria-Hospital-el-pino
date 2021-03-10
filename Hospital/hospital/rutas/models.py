from django.db import models
import json
from datetime import date
from django.utils import timezone


class RutaManager(models.Manager):
    def crear_ruta(self, equipo_asignado, fecha, ruta, direcciones_ordenadas, link, pacientes, distancia):
        ruta = self.create(equipo_asignado = equipo_asignado, fecha = fecha, ruta = ruta, direcciones_ordenadas = direcciones_ordenadas, link = link, distancia = distancia, pacientes = pacientes)
        return ruta

class Ruta(models.Model):
    id = models.AutoField(primary_key=True)
    equipo_asignado = models.CharField(default = 'Sin equipo', max_length=30)
    fecha = models.DateField(default= timezone.now)
    ruta = models.CharField(blank=True, max_length=2500)
    direcciones_ordenadas = models.CharField(default=" ", max_length=50000)
    distancia = models.FloatField(default=0.0)
    link = models.CharField(default = "", max_length=20000)
    pacientes = models.CharField(default= "", max_length=20000)
    pos_actual = models.IntegerField(default= 0)
    objects = RutaManager()

    def __str__(self):
        x = str(self.equipo_asignado) + str(self.fecha) + "(" + str(self.id) + ")"
        return x

    def get_ruta(self):
        return json.loads(self.ruta)

