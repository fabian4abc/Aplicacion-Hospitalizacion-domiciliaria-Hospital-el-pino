from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Paciente


class Paciente_Form_activo(forms.ModelForm):
	class Meta:
		model = Paciente

		fields=['id_tutor',
				'nombre',
				'apellido1',
				'apellido2',
				'rut',
				'comuna',
				'domicilio',
				'num_domicilio',
				'f_nacimiento',
				'desc',
				'activo',
				'episodio']