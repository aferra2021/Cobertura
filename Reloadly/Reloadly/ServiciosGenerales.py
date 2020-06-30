from django.http import HttpResponse,Http404
from django.shortcuts import render
from apps.RecargasCubacel.serviciosCubacel import recargaCubacel
from apps.RecargasNauta.serviciosNauta import recargasNauta
from apps.EtecsaTelefonoFijo.serviciosTelefonoFijo import recargasTelefonoFijo
from apps.CubacelTur.serviciosCubacelTur import recargaCubacelTur
from apps.CubacelSimTelefono.serviciosCubacelSimTelefono import transCubacelSimTelefono

def ServerManage(listTrans):
    cubacel=[]
    nauta=[]
    telefonoFijo=[]
    Cubaceltur=[]
    SimTelefono=[]
    for l in listTrans:
        if l.tipo=="Cubacel":
            cubacel.append(l)
        elif l.tipo=="Nauta":
            nauta.append(l)
        elif l.tipo=='TelefonoFijo':
            telefonoFijo.append(l)
        elif l.tipo=='CubacelTur':
            Cubaceltur.append(l)
        elif l.tipo=='SimTelefono':
            SimTelefono.append(l)
    ####################################################################################################################
    Json=recargaCubacel(cubacel)
    ####################################################################################################################
    Json.append(recargasNauta(nauta))
    ####################################################################################################################
        #recargasTelefonoFijo(telefonoFijo)
    ####################################################################################################################
        #recargaCubacelTur(Cubaceltur)
    ####################################################################################################################
        #transCubacelSimTelefono(SimTelefono)
    ####################################################################################################################
    return Json
