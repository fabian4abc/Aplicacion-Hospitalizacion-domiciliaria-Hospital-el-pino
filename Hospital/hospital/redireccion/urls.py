from django.conf.urls import url,re_path
from django.urls import path, include
from redireccion import views

urlpatterns =[

url(r'redirect/',views.redireccion,name="redireccion"),

]

