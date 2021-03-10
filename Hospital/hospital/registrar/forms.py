from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import formulario
from visita.models import Visita
from datetime import date, time,datetime

now=datetime.today()

class formulario_visita_esp(forms.ModelForm):

 	class Meta:
 		model = formulario

 		fields = [
 			'id_visita',
 			'id_especialista',
 			'detalle',
 			'h_inicio',
 			'antecedentes',
 			'red_apoyo',
 			'indice_barthel',
			'escala_braden',
			'escala_norton',
			'detalle',
			'evolucion',
			'pendientes',
			'comentarios',
			'nota',
			'id_paciente',
			'episodio',



 			]

 		