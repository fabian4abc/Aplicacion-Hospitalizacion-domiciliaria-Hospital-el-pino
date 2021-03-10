from django.db import models

class Visita(models.Model):
	fecha = models.DateField(null=False)
	id_paciente = models.IntegerField(null=False)
	status = models.IntegerField(null=False, default=0) #0 = Activa 1= Completa 
	equipo = models.CharField(max_length=20,null=False, default='Disponible') #0 = ninguno otro= id_equipo
	episodio = models.IntegerField(null=False, default=0)
	nombre = models.CharField(max_length=30, default="Sin asignar")
	
	observaciones = models.CharField(max_length=30000, default=" ")
	hora_inicio = models.CharField(max_length=20, default = " ")
	hora_termino = models.CharField(max_length=20, default = " ")
	
	apellido1=models.CharField(max_length=30, default="Sin asignar")
	apellido2=models.CharField(max_length=30, default="Sin asignar")
	rut = models.CharField(null=False,max_length=15, default="0")
	comuna= models.CharField(max_length=20, default="Sin asignar")
	domicilio=models.CharField(max_length=50, default="Sin asignar")
	num_domicilio=models.CharField(max_length=50, default="0")
	

class Tiempos(models.Model):
	item = models.CharField(max_length=20,null=False)
	tiempo = models.IntegerField(null=False, default=0)


class Llamar(models.Model):
	tel = models.CharField(max_length=20,null=False)
	correo = models.CharField(max_length=40,null=False)
	texto_explicativo = models.CharField(max_length=200,null=False)
