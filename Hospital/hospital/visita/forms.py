from django import forms
from .models import Visita, Tiempos

class Agendar(forms.ModelForm):
	class Meta:
		model = Visita

		fields=['fecha',
				'id_paciente',
				'episodio']

		widgets={

				'fecha':forms.DateInput(attrs={'class':'form-control','type':'date'}),
		}


class asignar_equipo(forms.ModelForm):

 	class Meta:
 		model = Visita

 		fields = [
 			'fecha',
 			'id_paciente',
 			'status',
 			'equipo'
 			]
 		widgets={

				'fecha':forms.DateInput(attrs={'class':'form-control','type':'hidden'}),
		}

class time(forms.ModelForm):

 	class Meta:
 		model = Tiempos

 		fields = [
 			'item',
 			'tiempo'
 			]

