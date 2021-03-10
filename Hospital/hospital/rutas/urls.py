from django.conf.urls import url,re_path
from django.urls import path, include
from rutas import views

urlpatterns = [  
    path('planificacion/', views.vista_optimizacion, name="planificar" ),
    url(r'optimizar/', views.optimizar_rutas, name="optimizar_rutas"),
    url(r'rutas/', views.ver_rutas, name="lista_rutas"),
]
