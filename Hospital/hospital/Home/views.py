from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
	def get(self,request,**kwargs):
		return render(request, 'main.html', context=None)


# Create your views here.
