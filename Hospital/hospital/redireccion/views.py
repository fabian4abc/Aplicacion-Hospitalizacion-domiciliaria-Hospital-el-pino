from django.shortcuts import render, get_object_or_404, reverse
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from usuarios.models import Paciente , Personal, Tutor, Perfil
from django.contrib.auth.models import User
from usuarios.views import Registro_View
from django.contrib.auth.decorators import login_required

@login_required
def redireccion(request):
	current_user = request.user
	queryset = get_object_or_404(Perfil, usuario_id = current_user.id)
	actual = queryset.rol

	if actual == "TUTOR":
		return HttpResponseRedirect(reverse('home_t'))	

	if actual == "PERSONAL":
		return HttpResponseRedirect(reverse('home_e'))

	if actual == "ADMINISTRADOR":
		return HttpResponseRedirect(reverse('dash'))

	if actual == "SuperAdmin":
		return HttpResponseRedirect(reverse('dash'))

	if actual != "TUTOR" or  actual != "PERSONAL" or actual != "ADMINISTRADOR" or actual != "SuperAdmin":
		return redirect(Registro_View)

	return render(request,"salto.html")
