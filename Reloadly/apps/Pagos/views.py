from django.shortcuts import render
from apps.Usuarios.models import TransferenciaActual
from django.http import HttpResponse
from Reloadly.ServiciosGenerales import ServerManage



# Create your views here.
def pagosGeneral(request):
    if request.method=='GET':
        listTrans=TransferenciaActual.objects.filter(cliente=request.user)
        #aki hay q mostrar todas las transferencias q el usuario a metido en el carrito
        return HttpResponse(render(request,'PagosTemplate/pagosGeneral.html',{'post':'True','ListTrans':listTrans}))
    else:
        #vamos asuponer q pague: ahora hay q hacer todad las transferencias q haya hecho ese usuario
        listTrans=TransferenciaActual.objects.filter(cliente=request.user)
        JsonCubacel=ServerManage(listTrans)
        for trans in JsonCubacel:
            if 'HTTPSConnectionPool' in trans.__str__():
                return HttpResponse(render(request, 'PagosTemplate/pagosDone.html',{'json':'Usted no tiene coneccion'}))
        #el pago se hizo
        #hay q eliminar las transferenciasactuales y agregar las permanentes

        return HttpResponse(render(request, 'PagosTemplate/pagosDone.html',{'json':JsonCubacel}))