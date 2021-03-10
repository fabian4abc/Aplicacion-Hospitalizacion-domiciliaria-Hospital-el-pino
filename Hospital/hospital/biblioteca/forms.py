from django import forms 
from .models import Archivo, Archivo_Unico


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ('nombre', 'file', )

        widgets={
        'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Inserte Nombre de Archivo'}),
        }


class DocumentFormUnico(forms.ModelForm):
    class Meta:
        model = Archivo_Unico
        fields = ('nombre', 'file', 'paciente' )

        widgets={
        'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Inserte Nombre de Archivo'}),
        }