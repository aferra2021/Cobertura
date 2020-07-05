from django.shortcuts import render
from apps.Usuarios.models import TransferenciaActual,TranferenciaGeneral,Contacto
from django.http import HttpResponse
from Reloadly.ServiciosGenerales import ServerManage
from django.contrib.auth.models import User




# Create your views here.
def pagosGeneral(request):
    if request.method=='GET':
        listTrans=TransferenciaActual.objects.filter(cliente=request.user)
        #aki hay q mostrar todas las transferencias q el usuario a metido en el carrito
        return HttpResponse(render(request,'PagosTemplate/pagosGeneral.html',{'post':'True','ListTrans':listTrans}))
    else:
        # vamos asuponer q pague: ahora hay q hacer todad las transferencias q haya hecho ese usuario
        listTrans = TransferenciaActual.objects.filter(cliente=request.user)
        JsonCubacel = ServerManage(listTrans)
        error = False
        """for trans in JsonCubacel:
            if 'Error' in trans.__str__():
                error=True"""
        # el pago se hizo
        # hay q eliminar las transferenciasactuales y agregar las permanentes
        if error:
            return HttpResponse(render(request, 'PagosTemplate/pagosDone.html', {'json': JsonCubacel}))
        else:
            cliente=User.objects.filter(username=request.user)
            for trans in listTrans:
                contacto=Contacto.objects.get(accountNumber=trans.accountNumber)
                if not contacto:
                    contacto = Contacto.objects.create(accountNumber=trans.accountNumber)
                    contacto.user.set(cliente)
                    contacto.save()

                TG=TranferenciaGeneral(tipo=trans.tipo,fecha=trans.fecha,cliente=trans.cliente,SendValue=trans.SendValue,contacto=contacto)
                TG.save()
                TA = TransferenciaActual.objects.get(pk=trans.pk)
                TA.delete()
            return HttpResponse(render(request, 'PagosTemplate/pagosDone.html', {'json': JsonCubacel}))
