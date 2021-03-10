from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from usuarios.models import Paciente, Personal
from usuarios.models import Tutor
from usuarios.models import Perfil
from visita.models import Visita
from django.contrib.auth.models import User
from registrar.forms import formulario_visita_esp
from especialista.views import visitas_programadas_esp
from visita.forms import  asignar_equipo
from datetime import date, time,datetime 
from registrar.models import formulario as fm
from django.contrib.auth.decorators import login_required

@login_required
def formulario(request, id=None):

	now = datetime. now()
	current_time = now.strftime("%H:%M:%S")
	now = datetime.today()
	current_user = request.user
	personal = Personal.objects.get(id_perfil=current_user.id)
	visita =  get_object_or_404(Visita, id=id)
	px = get_object_or_404(Paciente, id=visita.id_paciente)
	form = formulario_visita_esp(request.POST)

	edad_p = edad(px.f_nacimiento)
	if request.method == 'POST':
		form = formulario_visita_esp(request.POST)
		if form.is_valid():
			visita.status=1
			visita.save()
			form.save()
			return redirect(visitas_programadas_esp)
	context = {
		"id_visita": visita.id,
		"id_especialista": personal.id,
		"actual":current_user,
		"px":px,
		"form":form,
		"h_inicio":current_time,
		"id_paciente":px.id,
		"edad":edad_p
	}
		
	return render(request,'formulario_visita_esp.html',context)

@login_required
def ver_formulario(request, id=None):

	visita = get_object_or_404(Visita, id=id)
	frml = get_object_or_404(fm,id_visita=visita.id)
	paciente = Paciente.objects.get(id=frml.id_paciente)
	personal = Personal.objects.get(id=frml.id_especialista)
	user = User.objects.get(id=personal.id_perfil_id)
	context = {
		"f": frml,
		"v": visita,
		"user":user,
		"paciente":paciente
	}

	return render(request,'ver_formulario_detalle.html',context)

@login_required
def ver_registro_admin(request, id=None):
	px = get_object_or_404(Paciente, id=id)
	fx = Visita.objects.all()
	context = {
		"obj":px,
		"date_list":fx,
		"episodio": range(1,px.episodio+1),
		"count": 1,
	}
	return render(request,'ver_registro_admin.html',context)

@login_required
def ver_registro_tutor(request, id=None):
	px = get_object_or_404(Paciente, id=id)
	fx = Visita.objects.all()
	context = {
		"obj":px,
		"date_list":fx,
		"episodio": range(1,px.episodio+1),
		"count": 1,

	}
	return render(request,'ver_registro_tutor.html',context)


@login_required
def ver_episodio_numerado(request, id=None, id_paciente=None):
	aux = id
	fx = fm.objects.all()
	px = get_object_or_404(Paciente, id=id_paciente)
	context = {
		"aux":int(aux),
		"formulario":fx,
		"paciente":px,
	}
	return render(request,'ver_episodio_numerado.html',context)

@login_required
def ver_episodio_numerado_tutor(request, id=None, id_paciente=None):
	aux = id
	fx = fm.objects.all()
	px = get_object_or_404(Paciente, id=id_paciente)
	visita=Visita.objects.all()
	context = {
		"aux":int(aux),
		"formulario":fx,
		"paciente":px,
		"visita":visita,
	}
	return render(request,'ver_episodio_numerado_tutor.html',context)

@login_required
def ver_episodio_numerado_esp(request, id=None, id_paciente=None):
	aux = id
	fx = fm.objects.all().order_by('-id')
	px = get_object_or_404(Paciente, id=id_paciente)
	visita=Visita.objects.all()
	context = {
		"aux":int(aux),
		"formulario":fx,
		"paciente":px,
		"visita":visita,
	}
	return render(request,'ver_episodio_numerado_esp.html',context)


@login_required
def edad(naci):
    hoy = datetime.today()
    f_naci = datetime.strptime(naci,"%Y-%m-%d")
    if hoy < f_naci:
    	print("error en fecha nacimiento")
    else:
        ano = f_naci.year
        anno_hoy = hoy.year
        fecha = anno_hoy-ano
        return fecha

@login_required
def detalle_historial_visita_esp(request,id_visita=None):
	visita = Visita.objects.get(id=id_visita)
	form = fm.objects.get(id_visita=id_visita)
	personal = Personal.objects.get(id=form.id_especialista)
	user = User.objects.get(id=personal.id_perfil_id)
	context={
		"form":form,
		"personal":personal,
		"user":user,
		"visita":visita,
	}
	return render(request,"detalle_historial_esp.html",context)

@login_required
def detalle_historial_tutor(request,id_visita=None):
	visita = Visita.objects.get(id=id_visita)
	form = fm.objects.get(id_visita=id_visita)
	personal = Personal.objects.get(id=form.id_especialista)
	user = User.objects.get(id=personal.id_perfil_id)
	context={
		"form":form,
		"personal":personal,
		"user":user,
		"visita":visita,
	}
	return render(request,"detalle_historial_tutor.html",context)