from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Paciente


class tipo(forms.ModelForm):
	class Meta:
		model = Paciente

		fields=['tipo']