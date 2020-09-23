from django.http import HttpResponse,Http404
from django.shortcuts import render
from apps.RecargasCubacel.serviciosCubacel import recargaCubacel,PaquetesDatosCubacel
from apps.RecargasNauta.serviciosNauta import recargasNauta
from apps.EtecsaTelefonoFijo.serviciosTelefonoFijo import recargasTelefonoFijo
from apps.CubacelTur.serviciosCubacelTur import recargaCubacelTur
from apps.CubacelSimTelefono.serviciosCubacelSimTelefono import transCubacelSimTelefono
from apps.Usuarios.models import TransferenciaActual

def ServerManage(request):
    listTrans = TransferenciaActual.objects.filter(cliente=request.user)
    cubacel=[]
    nauta=[]
    paquetes=[]
    Json=[]
    """Reserva=[]
    telefonoFijo=[]
    Cubaceltur=[]
    SimTelefono=[]"""
    for l in listTrans:
        if l.tipo=="Recarga Cubacel" or l.tipo=="Saldo+Bono":
            cubacel.append(l)
        elif l.tipo=="Nauta":
            nauta.append(l)
        elif l.tipo=="Datos Moviles Cubacel":
            paquetes.append(l)
            # guardar el la tabla de reservas
#        elif l.tipo=='SimTelefono':
#            SimTelefono.append(l)
    ####################################################################################################################
    if cubacel:
        #print(recargaCubacel(cubacel))
        Json.append(recargaCubacel(cubacel))
    ####################################################################################################################
    if nauta:
        #print(recargasNauta(nauta))
        Json.append(recargasNauta(nauta))
    ####################################################################################################################
    if paquetes:
        Json.append(PaquetesDatosCubacel(paquetes))

    ####################################################################################################################
        #recargaCubacelTur(Cubaceltur)
    ####################################################################################################################
        #transCubacelSimTelefono(SimTelefono)
    ####################################################################################################################
    Carrito = TransferenciaActual.objects.filter(cliente=request.user)
    #if len(Carrito)!=0:
     #   return HttpResponse(render(request,'UsuariosTemplates/carrito.html',{'error':'error','cantidadCarrito': len(Carrito),'carrito':Carrito}))
    return HttpResponse(render(request,'Test.html',{'Json':Json,'cantidadCarrito': len(Carrito),'carrito':Carrito}))
