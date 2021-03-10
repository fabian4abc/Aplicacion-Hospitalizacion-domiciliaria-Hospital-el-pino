from django.db import models

class formulario(models.Model):
	id_visita = models.IntegerField(null=False)
	id_especialista = models.IntegerField(null=False)
	id_paciente = models.IntegerField(null=False,default=0)
	h_inicio=models.TimeField(null=False)
	h_termino=models.TimeField(null=False, auto_now_add=True)
	antecedentes=models.CharField(max_length=400,null=False,default="Vacio")
	red_apoyo=models.CharField(max_length=20,null=False,default="Vacio")
	indice_barthel=models.IntegerField(null=False,default=0)
	escala_braden=models.IntegerField(null=False,default=0)
	escala_norton=models.IntegerField(null=False,default=0)
	detalle = models.CharField(max_length=400,null=False,default="Vacio")
	evolucion = models.CharField(max_length=400,null=False,default="Vacio")
	pendientes = models.CharField(max_length=400,null=False,default="Vacio")
	comentarios = models.CharField(max_length=400,null=False,default="Vacio")
	nota = models.IntegerField(null=False,default=0)
	episodio = models.IntegerField(null=False,default=0)

