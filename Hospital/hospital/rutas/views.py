from django.shortcuts import render,redirect, reverse, HttpResponseRedirect
import json
import requests as req
import time
import math
import numpy as np
from datetime import date
from django.shortcuts import render
from .models import Ruta
from usuarios.models import Paciente
from visita.models import Visita
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import re


@login_required
def vista_optimizacion(request):
    visitas = Visita.objects.all()
    rutas = Ruta.objects.all()
    visitas_hoy = []
    rutas_hoy = []
    visitas_asignadas = []
    direc_mapa = []
    direcciones = []
    concatenar = ""
    x = 0
    for visita in visitas:
        if visita.fecha == date.today():
            visitas_hoy.append(visita)
            direcciones.append(((str(visitas_hoy[x].domicilio)).replace(" ", "+")+"+"+(str(visitas_hoy[x].num_domicilio)).replace(" ", "+")+","+(str(visitas_hoy[x].comuna)).replace(" ", "+")+",chile" ))
            direc_mapa.append((str(direcciones[x]) + "|marker-sm-" + str(x) + "||"))
            if visita.equipo != 'Disponible':
                visitas_asignadas.append(visita)
            x +=1
    for ruta in rutas:
        if ruta.fecha == date.today():
            rutas_hoy.append(ruta)

    if rutas_hoy:
        mapa = "https://www.mapquestapi.com/staticmap/v5/map?locations="+str(concatenar.join(direc_mapa)) +"&size=300,300@2x&key=K4YQLdWn9G3LkCzYAt0LDixd9T1J0MLL"
        context = {
            "rutas": 1,
            "mapa":mapa
        }
    elif visitas_asignadas:
        mapa = "https://www.mapquestapi.com/staticmap/v5/map?locations="+str(concatenar.join(direc_mapa)) +"&size=300,300@2x&key=K4YQLdWn9G3LkCzYAt0LDixd9T1J0MLL"
        context = {
            "visitas":1,
            "equipo":1,
            "mapa":mapa
        }
    elif visitas_hoy:
        mapa = "https://www.mapquestapi.com/staticmap/v5/map?locations="+str(concatenar.join(direc_mapa)) +"&size=300,300@2x&key=K4YQLdWn9G3LkCzYAt0LDixd9T1J0MLL"
        context = {
            "visitas":1,
            "mapa":mapa
        }
    else:
         context = {
        "no_visitas":1
    }    
    return render(request, "test.html", context)




@login_required
def optimizar_rutas(request):
    current_user = request.user

    Api1 = "https://us1.locationiq.com/v1/search.php?key=pk.0bcfdf18973ec7dc66d274a58578acb7"
    Api2 = "http://www.mapquestapi.com/directions/v2/routematrix?key=K4YQLdWn9G3LkCzYAt0LDixd9T1J0MLL"
    
    ubicaciones_sb = ["Hospital+y+CRS+El+Pino+-+Av.+Padre+Hurtado+13560,+San+Bernardo,+Región+Metropolitana+,chile"]
    ubicaciones_eb = ["Hospital+y+CRS+El+Pino+-+Av.+Padre+Hurtado+13560,+San+Bernardo,+Región+Metropolitana+,chile"]
    ubicaciones_lp = ["Hospital+y+CRS+El+Pino+-+Av.+Padre+Hurtado+13560,+San+Bernardo,+Región+Metropolitana+,chile"]

    req_api1_sb = [] #Request a la api 1 para el equipo de San Bernardo
    req_api1_sb_dict = [] #Request pasada a json
    req_api1_eb = [] #Request a la api 1 para el equipo de El Bosque
    req_api1_eb_dict = [] #Request pasada a json
    req_api1_lp = [] #Request a la api 1 para el equipo de La Pintana
    req_api1_lp_dict = [] #Request pasada a json
    
    visitas = Visita.objects.all()
    visitas_sb = [] #Visitas asinadas para el equipo de San Bernardo.
    visitas_eb = [] #Visitas asinadas para el equipo de El Bosque.
    visitas_lp = [] #Visitas asignadas para el equipo de La Pintana.
    visitas_hoy= [] #Visitas programadas para el día de hoy.

    pacientes_sb = []
    pacientes_eb = []
    pacientes_lp = []
    
    ruta_sb = 0
    ruta_eb = 0
    ruta_lp = 0

    contador = 0
    
    for visita in visitas:
        if visita.fecha == date.today():
            if visita.equipo == "SanBernardo":
                ubicaciones_sb.append((str(visita.domicilio)).replace(" ", "+")+"+"+(str(visita.num_domicilio)).replace(" ", "+")+","+(str(visita.comuna)).replace(" ", "+")+",chile" )
                #req_api1_sb.append(req.get(url=Api1, params = {'q':ubicaciones_sb[contador], 'accept-language':'es', 'format':'json'}))
                #req_api1_sb_dict.append(req_api1_sb[contador].json())
                visitas_sb.append(visita)
                pacientes_sb.append(visita.id_paciente)
            if visita.equipo == "ElBosque":
                ubicaciones_eb.append((str(visita.domicilio)).replace(" ", "+")+"+"+(str(visita.num_domicilio)).replace(" ", "+")+","+(str(visita.comuna)).replace(" ", "+")+",chile" )
                #req_api1_eb.append(req.get(url=Api1, params = {'q':ubicaciones_eb[contador], 'accept-language':'es', 'format':'json'}))
                #req_api1_eb_dict.append(req_api1_eb[contador].json())
                visitas_eb.append(visita)
                pacientes_eb.append(visita.id_paciente)
            if visita.equipo == "LaPintana":
                ubicaciones_lp.append((str(visita.domicilio)).replace(" ", "+")+"+"+(str(visita.num_domicilio)).replace(" ", "+")+","+(str(visita.comuna)).replace(" ", "+")+",chile" )
                #req_api1_lp.append(req.get(url=Api1, params = {'q':ubicaciones_lp[contador], 'accept-language':'es', 'format':'json'}))
                #req_api1_lp_dict.append(req_api1_lp[contador].json())
                visitas_lp.append(visita)
                pacientes_lp.append(visita.id_paciente)
            visitas_hoy.append(visita)
                
    if visitas_sb:
        data_api2_sb = {
            "locations": ubicaciones_sb,
            "options":{
                "allToAll": True
            }
        }
        
        x = req.post(Api2, json = data_api2_sb)
        x_dict = json.loads(x.text)
        matriz_d = x_dict['distance']
        nodos = len(ubicaciones_sb)

        ruta = [0]
        distancia = 0
        visitados = []
        for l in range(0, nodos):
            visitados.append(0)
        i = 0
        for z in range(nodos):
            temp_val = 0
            temp_j = 0
            ol = 0
            for j in range(nodos):
                if visitados[j] == 0:
                    if matriz_d[i][j] != 0:
                        if j != 0:
                            if ol == 0:
                                temp_val = matriz_d[i][j]
                                temp_j = j
                                ol = 1
                    if matriz_d[i][j] != 0:
                        if matriz_d[i][j] < temp_val:
                            temp_val = matriz_d[i][j]
                            temp_j = j			
                if j+1 == nodos:
                    ruta.append(temp_j)
                    if temp_j == 0:
                        distancia += matriz_d[i][0]
                    i = temp_j
                    visitados[temp_j] = 1
                    distancia += temp_val	

        distancia = f"{distancia:.2f}"
        distancia_f = (float(distancia))*1.60934 #millas a kilometros
        distancia_f = f"{distancia_f:.2f}"
        direcciones_ordenadas = []
        pacientes_ordenados = []
        direc_mapa = []
      
        
        for x in range(len(ruta)):
            direcciones_ordenadas.append(ubicaciones_sb[ruta[x]])
            if x == 0:
                direc_mapa.append(str(direcciones_ordenadas[x]) + "|marker-sm-D51A1A-A20000||")
            if x>0:
                if x == len(ruta)-1:
                    
                    direc_mapa.append(str(direcciones_ordenadas[x]) + "|marker-sm-D51A1A-A20000||")
                    break
                direc_mapa.append(str(direcciones_ordenadas[x]) + "|marker-sm-" + str(x) + "||")
                if x<len(ruta)-1:
                    pacientes_ordenados.append(pacientes_sb[ruta[x]-1])
    

        ruta_json = json.dumps(ruta)
        lista = "/"
        concatenar = ""


        link = "https://www.google.com/maps/dir/" + lista.join(direcciones_ordenadas)
        mapa_sb = "https://www.mapquestapi.com/staticmap/v5/map?locations="+str(concatenar.join(direc_mapa)) +"&size=300,300@2x&key=K4YQLdWn9G3LkCzYAt0LDixd9T1J0MLL"
        ruta_sb = Ruta.objects.crear_ruta("SanBernardo", date.today(), ruta_json, direcciones_ordenadas, link, pacientes_ordenados, distancia_f)
        print(mapa_sb)
    
    if visitas_eb:
        data_api2_eb = {
            "locations": ubicaciones_eb,
            "options":{
                "allToAll": True
            }
        }
        
        x = req.post(Api2, json = data_api2_eb)
        x_dict = json.loads(x.text)
        matriz_d = x_dict['distance']
        nodos = len(ubicaciones_eb)

        ruta = [0]
        distancia = 0
        visitados = []
        for l in range(0, nodos):
            visitados.append(0)
        i = 0
        for z in range(nodos):
            temp_val = 0
            temp_j = 0
            ol = 0
            for j in range(nodos):
                if visitados[j] == 0:
                    if matriz_d[i][j] != 0:
                        if j != 0:
                            if ol == 0:
                                temp_val = matriz_d[i][j]
                                temp_j = j
                                ol = 1
                    if matriz_d[i][j] != 0:
                        if matriz_d[i][j] < temp_val:
                            temp_val = matriz_d[i][j]
                            temp_j = j			
                if j+1 == nodos:
                    ruta.append(temp_j)
                    if temp_j == 0:
                        distancia += matriz_d[i][0]
                    i = temp_j
                    visitados[temp_j] = 1
                    distancia += temp_val	

        distancia = f"{distancia:.2f}"
        distancia_f = (float(distancia))*1.60934 #millas a kilometros
        distancia_f = f"{distancia_f:.2f}"
        direcciones_ordenadas = []
        pacientes_ordenados = []
        direc_mapa = []
      
        
        for x in range(len(ruta)):
            direcciones_ordenadas.append(ubicaciones_eb[ruta[x]])
            if x == 0:
                direc_mapa.append(str(direcciones_ordenadas[x]) + "|marker-sm-D51A1A-A20000||")
            if x>0:
                if x == len(ruta)-1:
                    direc_mapa.append(str(direcciones_ordenadas[x]) + "|marker-sm-D51A1A-A20000||")
                    break
                direc_mapa.append(str(direcciones_ordenadas[x]) + "|marker-sm-" + str(x) + "||")
                if x<len(ruta)-1:
                    pacientes_ordenados.append(pacientes_eb[ruta[x]-1])

        ruta_json = json.dumps(ruta)
        lista = "/"
        concatenar = ""


        link = "https://www.google.com/maps/dir/" + lista.join(direcciones_ordenadas)
        mapa_eb = "https://www.mapquestapi.com/staticmap/v5/map?locations="+str(concatenar.join(direc_mapa)) +"&size=300,300@2x&key=K4YQLdWn9G3LkCzYAt0LDixd9T1J0MLL"
        ruta_eb = Ruta.objects.crear_ruta("ElBosque", date.today(), ruta_json, direcciones_ordenadas, link, pacientes_ordenados, distancia_f)

    if visitas_lp:
        data_api2_lp = {
            "locations": ubicaciones_lp,
            "options":{
                "allToAll": True
            }
        }
        x = req.post(Api2, json = data_api2_lp)
        x_dict = json.loads(x.text)
        matriz_d = x_dict['distance']
        nodos = len(ubicaciones_lp)

        ruta = [0]
        distancia = 0
        visitados = []
        for l in range(0, nodos):
            visitados.append(0)
        i = 0
        for z in range(nodos):
            temp_val = 0
            temp_j = 0
            ol = 0
            for j in range(nodos):
                if visitados[j] == 0:
                    if matriz_d[i][j] != 0:
                        if j != 0:
                            if ol == 0:
                                temp_val = matriz_d[i][j]
                                temp_j = j
                                ol = 1
                    if matriz_d[i][j] != 0:
                        if matriz_d[i][j] < temp_val:
                            temp_val = matriz_d[i][j]
                            temp_j = j			
                if j+1 == nodos:
                    ruta.append(temp_j)
                    if temp_j == 0:
                        distancia += matriz_d[i][0]
                    i = temp_j
                    visitados[temp_j] = 1
                    distancia += temp_val	

        distancia = f"{distancia:.2f}"
        distancia_f = (float(distancia))*1.60934 #millas a kilometros
        distancia_f = f"{distancia_f:.2f}"
        ruta_json = json.dumps(ruta)

        direcciones_ordenadas = []
        pacientes_ordenados = []
        
        direc_mapa = []
      
        for x in range(len(ruta)):
            direcciones_ordenadas.append(ubicaciones_lp[ruta[x]])
            if x == 0:
                direc_mapa.append(str(direcciones_ordenadas[x]) + "|marker-sm-D51A1A-A20000||")
            if x>0:
                if x == len(ruta)-1:
                    direc_mapa.append(str(direcciones_ordenadas[x]) + "|marker-sm-D51A1A-A20000||")
                    break
                direc_mapa.append(str(direcciones_ordenadas[x]) + "|marker-sm-" + str(x) + "||")
                if x<len(ruta)-1:
                    pacientes_ordenados.append(pacientes_lp[ruta[x]-1])

        ruta_json = json.dumps(ruta)
        lista = "/"
        concatenar = ""


        link = "https://www.google.com/maps/dir/" + lista.join(direcciones_ordenadas)
        mapa_lp = "https://www.mapquestapi.com/staticmap/v5/map?locations="+str(concatenar.join(direc_mapa)) +"&size=300,300@2x&key=K4YQLdWn9G3LkCzYAt0LDixd9T1J0MLL"
        ruta_lp = Ruta.objects.crear_ruta("LaPintana", date.today(), ruta_json, direcciones_ordenadas, link, pacientes_ordenados, distancia_f)
        
    
    if ruta_sb and ruta_eb and ruta_lp:
        context = {
            "sb":ruta_sb,
            "eb":ruta_eb,
            "lp":ruta_lp,
            "mapa_sb":mapa_sb,
            "mapa_eb":mapa_eb,
            "mapa_lp":mapa_lp
        }
    elif ruta_sb and ruta_eb:
        context = {
            "sb":ruta_sb,
            "eb":ruta_eb,
            "mapa_sb":mapa_sb,
            "mapa_eb":mapa_eb
        }
    elif ruta_sb and ruta_lp:
        context = {
            "sb":ruta_sb,
            "lp":ruta_lp,
            "mapa_sb":mapa_sb,
            "mapa_lp":mapa_lp
        }
    elif ruta_eb and ruta_lp:
        context = {
            "eb":ruta_eb,
            "lp":ruta_lp,
            "mapa_eb":mapa_eb,
            "mapa_lp":mapa_lp
        }
    elif ruta_sb:
        context = {
            "sb":ruta_sb,
            "mapa_sb":mapa_sb
        }
    elif ruta_eb:
        context = {
            "eb":ruta_eb,
            "mapa_eb":mapa_eb
        }
    elif ruta_lp:
        context = {
            "lp":ruta_lp,
            "mapa_lp":mapa_lp
        }
    elif visitas_hoy:
        context = {
            "no_ruta": 1,
            "visitas_hoy": 1
        }
    else:
        context = {
            "no_equipo":1
        }
    return render(request, "rutas_optimizadas.html", context)




@login_required
def ver_rutas(request):
    rutas = Ruta.objects.all()
    pacientes = Paciente.objects.all()
    n_pacientes = []

    for ruta in rutas:
        temp=[]
        for a in re.split(r'\W+', str(ruta.pacientes)):
            if a.isdigit():
                temp.append(Paciente.objects.get(id=int(a)))
        for x in range(len(temp)):
            tempo = str(temp[x].nombre)+ " " +str(temp[x].apellido1) + " " + str(temp[x].apellido2)   
            a = a + "<|||>" + tempo
        n_pacientes.append(a)
    context = {
        "rutas":rutas,
        "pacientes":n_pacientes
    }
    return render(request, "lista_rutas.html", context)

    

