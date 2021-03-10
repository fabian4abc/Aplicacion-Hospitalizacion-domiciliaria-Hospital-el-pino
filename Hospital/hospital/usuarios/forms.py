from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil , Tutor , Paciente, Personal
from django.contrib.auth.models import User


class Registro_Form(UserCreationForm):
	first_name = forms.CharField(max_length=140, required = True)
	last_name = forms.CharField(max_length=140, required=False)
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = [
			 'username',
			 'email',
			 'first_name',
			 'last_name',
			 'password1',
			 'password2'
			 ]

class Perfil_Form(forms.ModelForm):
	class Meta:
		ROL=(
			('PERSONAL','Personal'),
			('TUTOR','Tutor'),
			('ADMINISTRADOR','Administrador'))
		model = Perfil
		fields=['rol',
				'tel']
		widgets={
		
		'rol':forms.Select(choices=ROL,attrs={'class':'form-control'}),
		'tel':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese número telefónico '}),
		}


class Paciente_Form(forms.ModelForm):
	class Meta:
		COMUNA=(("La Pintana","La Pintana"),
				("San Bernardo","San Bernardo"),
				("El Bosque","El Bosque"))

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
				'desc']

		widgets ={
				'nombre':forms.TextInput(attrs={'class':'form-control'}),
				'apellido1':forms.TextInput(attrs={'class':'form-control'}),
				'apellido2':forms.TextInput(attrs={'class':'form-control'}),
				'rut':forms.TextInput(attrs={'class':'form-control',"id":"rut", "required oninput":"checkRut(this)", "maxlength":"10"}),
				'comuna':forms.Select(choices=COMUNA,attrs={'class':'form-control'}),
				'domicilio':forms.TextInput(attrs={'class':'form-control'}),
				'num_domicilio':forms.TextInput(attrs={'class':'form-control'}),
				'f_nacimiento':forms.DateInput(attrs={'class':'form-control','type':'date'}),
				'desc':forms.TextInput(attrs={'class':'form-control','type':'textarea'}),

				}

class Tutor_Form(forms.ModelForm):
	class Meta:
		COMUNA=(("La Pintana","La Pintana"),
				("San Bernardo","San Bernardo"),
				("El Bosque","El Bosque"))

		model = Tutor

		fields=['id_perfil',
				'rut',
				'comuna',
				'domicilio',
				'num_domicilio',
				'f_nacimiento']

		widgets={
				'rut':forms.TextInput(attrs={'class':'form-control',"id":"rut", "required oninput":"checkRut(this)", "maxlength":"10"}),
				'comuna':forms.Select(choices=COMUNA,attrs={'class':'form-control'}),
				'domicilio':forms.TextInput(attrs={'class':'form-control'}),
				'num_domicilio':forms.TextInput(attrs={'class':'form-control'}),
				'f_nacimiento':forms.DateInput(attrs={'class':'form-control','type':'date'})
		}

class Personal_Form(forms.ModelForm):
	class Meta:
		ESPECIALIDAD=(('ENFERMERO','Enfermero'),('TECNICO','Técnico'),('KINESIOLOGO','Kinesiologo'), ('MEDICO','Médico'))
		model = Personal
		fields =['id_perfil','rut','especialidad','file']
		widgets ={
			'rut':forms.TextInput(attrs={'class':'form-control',"id":"rut", "required oninput":"checkRut(this)", "maxlength":"10"}),
			'especialidad': forms.Select(choices=ESPECIALIDAD,attrs={'class':'form-control'})
		}