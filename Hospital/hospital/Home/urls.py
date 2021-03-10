from django.conf.urls import url,re_path
from django.urls import path, include
from Home import views

urlpatterns =[
url(r'^$', views.HomeView.as_view(),name="main"),
path('accounts/', include('usuarios.urls')),
path('accounts/', include('django.contrib.auth.urls')),


]