from django.shortcuts import render, get_object_or_404,redirect, reverse, HttpResponseRedirect
from usuarios.models import Paciente
from visita.models import Visita, Tiempos, Llamar
from usuarios.models import Tutor,Personal
from usuarios.models import Perfil
from .forms import  Agendar, asignar_equipo, time
from lista.views import usuarios_listpa
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date
from django.contrib.auth.models import Group
from registrar.models import formulario
from django.contrib.auth.decorators import login_required

@login_required
def agendar_visita(request, id=None):
    aux = Paciente.objects.get(id=id)
    eq = Visita.objects.all()
    zxc = "Disponible"
    ep = aux.episodio
    
    nom = aux.nombre
    ape1 = aux.apellido1
    ape2 = aux.apellido2
    rut = aux.rut
    com = aux.comuna
    dom = aux.domicilio
    ndom = aux.num_domicilio

    for z in eq:
        if z.id_paciente == aux.id:
            if z.equipo != "Disponible":
                zxc = z.equipo
    
    if request.method == 'POST':

        if request.POST.get('periosidad') == "2vdAMPM":
                      
            fecha_inicial = request.POST.get('fecha')
            paciente = request.POST.get('id_paciente')
            
            
            for i in range(2):
                visita=Visita()
                visita.id_paciente = paciente
                visita.fecha = fecha_inicial
                visita.equipo = zxc
                visita.episodio = ep
                
                visita.nombre = nom
                visita.apellido1 = ape1
                visita.apellido2 = ape2
                visita.rut = rut
                visita.comuna = com
                visita.domicilio = dom
                visita.num_domicilio = ndom
                visita.save()
                print("entro")
        
        if request.POST.get('periosidad') == "0":
            fecha_inicial=request.POST.get('fecha')
            paciente=request.POST.get('id_paciente')
            visita=Visita()
            visita.id_paciente = paciente
            visita.fecha = fecha_inicial
            visita.equipo = zxc
            visita.episodio = ep

            visita.nombre = nom
            visita.apellido1 = ape1
            visita.apellido2 = ape2
            visita.rut = rut
            visita.comuna = com
            visita.domicilio = dom
            visita.num_domicilio = ndom
            visita.save()

        if request.POST.get('periosidad')=="2vsSA":
            fecha_inicial = request.POST.get('fecha')
            f_inicial = datetime.strptime(fecha_inicial,"%Y-%m-%d")

            fecha_sig = f_inicial + timedelta(days=2)
            paciente = request.POST.get('id_paciente')
           
            visita = Visita()
            visita.id_paciente = paciente
            visita.fecha = fecha_inicial
            visita.equipo = zxc
            visita.episodio = ep
            visita.nombre = nom
            visita.apellido1 = ape1
            visita.apellido2 = ape2
            visita.rut = rut
            visita.comuna = com
            visita.domicilio = dom
            visita.num_domicilio = ndom
            visita.save()

            visita = Visita()
            visita.id_paciente = paciente
            visita.fecha = fecha_sig
            visita.equipo = zxc
            visita.episodio = ep
            visita.nombre = nom
            visita.apellido1 = ape1
            visita.apellido2 = ape2
            visita.rut = rut
            visita.comuna = com
            visita.domicilio = dom
            visita.num_domicilio = ndom
            visita.save()

        if request.POST.get('periosidad') == "2vsSE":
            fecha_inicial = request.POST.get('fecha')
            f_inicial = datetime.strptime(fecha_inicial,"%Y-%m-%d")

            fecha_sig = f_inicial + timedelta(days=1)
            paciente=request.POST.get('id_paciente')
           
            visita = Visita()
            visita.id_paciente = paciente
            visita.fecha = fecha_inicial
            visita.equipo = zxc
            visita.episodio = ep
            visita.nombre = nom
            visita.apellido1 = ape1
            visita.apellido2 = ape2
            visita.rut = rut
            visita.comuna = com
            visita.domicilio = dom
            visita.num_domicilio = ndom
            visita.save()

            visita = Visita()
            visita.id_paciente = paciente
            visita.fecha = fecha_sig
            visita.equipo = zxc
            visita.episodio = ep
            visita.nombre = nom
            visita.apellido1 = ape1
            visita.apellido2 = ape2
            visita.rut = rut
            visita.comuna = com
            visita.domicilio = dom
            visita.num_domicilio = ndom
            visita.save()
        

        if request.POST.get('periosidad')=="3vsSA":
            fecha_inicial = request.POST.get('fecha')
            f_inicial = datetime.strptime(fecha_inicial,"%Y-%m-%d")

            fecha_2 = f_inicial + timedelta(days=2)
            fecha_3 = fecha_2 + timedelta(days=2)
            paciente=request.POST.get('id_paciente')
           
            visita = Visita()
            visita.id_paciente = paciente
            visita.fecha = fecha_inicial
            visita.equipo = zxc
            visita.episodio = ep
            visita.nombre = nom
            visita.apellido1 = ape1
            visita.apellido2 = ape2
            visita.rut = rut
            visita.comuna = com
            visita.domicilio = dom
            visita.num_domicilio = ndom
            visita.save()

            visita = Visita()
            visita.id_paciente = paciente
            visita.fecha = fecha_2
            visita.equipo = zxc
            visita.episodio = ep
            visita.nombre = nom
            visita.apellido1 = ape1
            visita.apellido2 = ape2
            visita.rut = rut
            visita.comuna = com
            visita.domicilio = dom
            visita.num_domicilio = ndom
            visita.save()

            visita = Visita()
            visita.id_paciente = paciente
            visita.fecha = fecha_3
            visita.equipo = zxc
            visita.episodio = ep
            visita.nombre = nom
            visita.apellido1 = ape1
            visita.apellido2 = ape2
            visita.rut = rut
            visita.comuna = com
            visita.domicilio = dom
            visita.num_domicilio = ndom
            visita.save()

        
        if request.POST.get('periosidad')=="3vsSE":
            fecha_inicial=request.POST.get('fecha')
            f_inicial=datetime.strptime(fecha_inicial,"%Y-%m-%d")

            fecha_2 = f_inicial + timedelta(days=1)
            fecha_3 = fecha_2 + timedelta(days=1)
            paciente=request.POST.get('id_paciente')
           
            visita=Visita()
            visita.id_paciente = paciente
            visita.fecha = fecha_inicial
            visita.equipo = zxc
            visita.episodio = ep
            visita.nombre = nom
            visita.apellido1 = ape1
            visita.apellido2 = ape2
            visita.rut = rut
            visita.comuna = com
            visita.domicilio = dom
            visita.num_domicilio = ndom
            visita.save()

            visita=Visita()
            visita.id_paciente = paciente
            visita.fecha = fecha_2
            visita.equipo = zxc
            visita.episodio = ep
            visita.nombre = nom
            visita.apellido1 = ape1
            visita.apellido2 = ape2
            visita.rut = rut
            visita.comuna = com
            visita.domicilio = dom
            visita.num_domicilio = ndom
            visita.save()

            visita=Visita()
            visita.id_paciente = paciente
            visita.fecha = fecha_3
            visita.equipo = zxc
            visita.episodio = ep
            visita.nombre = nom
            visita.apellido1 = ape1
            visita.apellido2 = ape2
            visita.rut = rut
            visita.comuna = com
            visita.domicilio = dom
            visita.num_domicilio = ndom
            visita.save()
                
        return redirect(visita_paciente_admin,id)
    context={
            "px":aux,
            "eq":zxc
        }
    return render(request,"agendar_visita.html",context)


@login_required
def agendar_lista(request):
    queryset = Visita.objects.all()
    instance = Paciente.objects.all()
    qset = request.GET.get("buscar")
    user = Paciente.objects.filter(rut = qset)
    current_user = request.user

    if user.count() < 1:
        instance = Paciente.objects.all()
    else:
        instance = user 
    context = {

        "date_list": queryset,
        "px": instance,
    }	
    return render(request,"agendar_lista.html",context)
 
@login_required    
def visita_paciente(request):
    queryset = Visita.objects.all()
    instance = get_object_or_404(Tutor, id_perfil_id = current_user.id)
    tx =  get_object_or_404(Tutor, id_perfil_id = current_user.id)
    pax = instance = get_object_or_404(Paciente, id_tutor_id = tx.id)
    current_user = request.user
    px = Paciente.objects.all()
   
    context = {
        "date_list": queryset,
        "px": px,
        "aux":instance.id,
        "paciente":pax,
        "actual": current_user,
    }	
    return render(request,"visita_paciente.html",context)

@login_required
def visita_paciente_admin(request, id=None):
    px = Paciente.objects.get(id=id)
    queryset = Visita.objects.all()
    tx = Tutor.objects.get(id=px.id_tutor_id)
    usr = get_object_or_404(User, id=tx.id_perfil_id)
    tel = get_object_or_404(Perfil, id=tx.id_perfil_id)
    context = {
        "date_list": queryset,
        "obj": px,
        "usr":usr,
        "tx":tx,
        "tel":tel,
    }	
    return render(request,"registro_visita_adm.html",context)

@login_required
def borrar_fecha(request,id=None):
    instance = get_object_or_404(Visita, id=id)
    id_p=instance.id_paciente
    instance.delete()
    messages.error(request, "Successfully deleted")
    return redirect(visita_paciente_admin,id_p)

@login_required
def borrar_lista(request,id=None):
    instance = get_object_or_404(Visita, id=id)
    id_p=instance.id_paciente
    instance.delete()
    messages.error(request, "Successfully deleted")
    return redirect(agendar_lista)

@login_required
def visita_update(request, id=None, id_paciente=None):
    aux = Visita.objects.get(id=id)	
    instance = get_object_or_404(Paciente, id=id_paciente)
    if request.method=='POST':
        f= request.POST.get('fecha')
        aux.fecha=f
        aux.save()
        return redirect(visita_paciente_admin,instance.id)
    return render(request,"agendar_update.html",{"id_paciente":aux.id_paciente,"status":aux.status})

@login_required
def reagendar(request):
    query = 0
    cont = Llamar.objects.count()
    if cont >0:
        query = get_object_or_404(Llamar)
    context = {
        "cont": cont,
        "i":query,
    }
    return render(request,"reagendar.html", context)

@login_required
def visita_paciente_detalle(request, id=None):
    current_user = request.user
    tx =  get_object_or_404(Tutor, id_perfil_id = current_user.id)
    px = instance = get_object_or_404(Paciente, id_tutor_id = tx.id)
    queryset = get_object_or_404(Visita, id=id)
    aux = get_object_or_404(formulario, id_visita=queryset.id)
    personal = Personal.objects.get(id=aux.id_especialista)
    user = User.objects.get(id=personal.id_perfil_id)
    context = {
        "visita": queryset,
        "form":aux,
        "paciente":px,
        "user":user
    }
    return render(request,"visita_paciente_detalle.html",context)

@login_required
def agendar_lista_hoy(request):
    queryset = Visita.objects.all()
    instance = Paciente.objects.all()
    hoy = date.today()
    group = Group.objects.all()
    if request.method=='POST':
        if request.POST.getlist('id_visita'):
            visita=request.POST.getlist('id_visita')
            grupo=request.POST.get('equipo')
            for i in visita:
                fecha=Visita.objects.get(id=i)
                f=fecha.fecha
                id_p=fecha.id_paciente
                fecha.status=0
                fecha.fecha=f
                fecha.id_paciente=id_p
                fecha.equipo=grupo
                fecha.save()
    context = {
        "date_list": queryset,
        "px": instance,
        "hoy":hoy,
        "group":group,
    }	
    return render(request,"agendar_lista_hoy.html",context)

@login_required
def tiempos(request):
    lista = Tiempos.objects.all()
    form = time(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('tiempos'))
    context = {
        "time":lista,
        "form":form
    }

    return render(request,'tiempos.html',context)

@login_required
def eliminar_tiempo(request,id):
    tiempo = get_object_or_404(Tiempos, id=id)
    if request.method == "POST":
        tiempo.delete()
        return redirect(tiempos)
    context = { 
      "t":tiempo,
    }
    return render(request,'delete_time.html',context)


@login_required
def visita_detalles(request,id=None):
    registro = get_object_or_404(formulario, id_visita=id)    
    context = {
        "f":registro,
    }
    return render(request,'visita_detalles_registro_adm.html',context)

@login_required
def tiempo_update(request, id=None):
    aux = Tiempos.objects.get(id=id) 
    if request.method=='GET':
        form=time(instance=aux)
    else:
        form=time(request.POST,instance=aux)     
        if form.is_valid():
            form.save()
        return redirect(tiempos)
    context = {
        "form":form,
        "id":aux.id,
        "item":aux.item,
        "t":aux.tiempo
    }
    return render(request,"tiempo_update.html",context)