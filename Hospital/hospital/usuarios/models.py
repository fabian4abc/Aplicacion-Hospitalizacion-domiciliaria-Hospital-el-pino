from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class Perfil(models.Model):
	usuario = models.OneToOneField(User,on_delete=models.CASCADE)
	rol = models.CharField(null=False,max_length=20)
	tel = models.CharField(null=False, max_length=20)
	umovil = models.CharField(default="Homero", max_length=20)
	cmovil = models.CharField(default="12345", max_length=20)

	def __str__(self):
		return str(self.usuario.username)


class Tutor(models.Model):
	id_perfil = models.ForeignKey(Perfil, default=None,on_delete=models.CASCADE)
	rut = models.CharField( null=False,max_length=15)
	comuna= models.CharField(max_length=20)
	domicilio=models.CharField(max_length=50)
	num_domicilio=models.CharField(max_length=50)
	f_nacimiento=models.CharField(max_length=20)
	
	def __str__(self):
		return str(self.id_perfil.usuario.username)
	

class Paciente(models.Model):
	id_tutor= models.ForeignKey(Tutor,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=30)
	apellido1=models.CharField(max_length=30)
	apellido2=models.CharField(max_length=30)
	rut = models.CharField(null=False,max_length=15)
	comuna= models.CharField(max_length=20)
	domicilio=models.CharField(max_length=50)
	num_domicilio=models.CharField(max_length=50)
	f_nacimiento=models.CharField(max_length=20)
	desc=models.CharField(max_length=100)
	activo=models.IntegerField(null=False, default=1)
	episodio=models.IntegerField(null=False, default=1)
	tipo=models.CharField(max_length=30, default="Vacio")

	
	def __str__(self):
		return self.nombre
	

class Personal(models.Model):
	id_perfil = models.ForeignKey(Perfil, default=None,on_delete=models.CASCADE)
	rut = rut = models.CharField(null=False,max_length=15)
	especialidad=models.CharField(max_length=20)
	file = models.FileField(upload_to='archivos/personal')

	def __str__(self):
		return str(self.id_perfil.usuario.username)




@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()





# Create your models here. 

