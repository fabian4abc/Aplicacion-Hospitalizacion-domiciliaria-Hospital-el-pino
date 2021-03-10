from django.conf.urls import url,re_path
from django.urls import path, include
from dashboard import views

urlpatterns =[

url(r'home/',views.home,name="dash"),
url(r'data/consulta',views.get_data_consulta,name="consulta"),
url(r'equipo/detalle/(?P<id>\d+)$',views.equipo_dash,name="equipo_dash"),


]