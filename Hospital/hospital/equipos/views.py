from django.shortcuts import render, redirect
from django.contrib.auth.models import Group		
from usuarios.models import Personal, Perfil
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required





@login_required
def Listar_equipo_view(request):	
	group = Group.objects.all()
	if request.POST.get('nombre_equipo'):
		nombre=request.POST.get('nombre_equipo')
		group = Group.objects.create(name=nombre)
		group.save()
		return redirect(Listar_equipo_view)
	else:
		return render(request,'listar_equipo.html',{'group':group})
		
	return render(request,'listar_equipo.html',{'group':group})






@login_required
def Ingreso_usuarios(request,id):
	
	group=Group.objects.get(id=id)
	disp=Group.objects.get(name='Disponible')
	if request.method=='POST':
		if request.POST.getlist('id_usuario'):
			id_user=request.POST.getlist('id_usuario')
			for i in id_user:
				user=User.objects.get(id=i)
				group.user_set.add(user)
				disp.user_set.remove(user)
		else:
			if request.POST.getlist('id_usuario_s'):
				id_user=request.POST.getlist('id_usuario_s')
				for i in id_user:
					user=User.objects.get(id=i)
					disp.user_set.add(user)
					group.user_set.remove(user)	

	disponible=User.objects.filter(groups__name='Disponible')
	equipo=User.objects.filter(groups__id=id)
	personal=Personal.objects.all()



	return render(request,"ingreso_usuarios_grupo.html",{'disponible':disponible,'personal':personal,'equipo':equipo,'group':group})


@login_required
def Eliminar_equipo(request,id):
	group=Group.objects.get(id=id)
	dispgroup=Group.objects.get(name='Disponible')
	if request.method=='POST':
		disp=User.objects.filter(groups__id=id)
		for d in disp:
			dispgroup.user_set.add(d)
		group.delete()
		return redirect(Listar_equipo_view)
	return render(request,"eliminar_equipo.html",{'group':group})