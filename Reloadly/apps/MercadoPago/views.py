from django.shortcuts import render
from apps.Usuarios.models import TransferenciaActual,TranferenciaGeneral,Contacto
from django.http import HttpResponse
from Reloadly.ServiciosGenerales import ServerManage
from django.contrib.auth.models import User
import requests
from .ServiciosMercadoPago import ObtenerCliente

# Create your views here.
#    //access_token=TEST-3968442574725364-052821-0a162b8a21c4dbd43f48933d227339ce-468607165'

def pagosGeneral(request):
    response = ObtenerCliente()
    return HttpResponse(render(request, 'PagosTemplate/pagosDone.html', {'json': response.json()}))



""" url = "https://api.mercadopago.com/v1/customers?access_token=TEST-3968442574725364-052821-0a162b8a21c4dbd43f48933d227339ce-468607165"
    payload = {
        "email": "brwwo@gmail.com",
        "first_name": "Bsruce",
        "last_name": "Wasyne",
        "phone": {
            "area_code": "023",
            "number": "12345638"
        },
        "identification": {
            "type": "DNI",
            "number": "12343672"
        },
        "address": {
            "zip_code": "SG1 2AX",
            "street_name": "Old Knebworth Ln"
        },
        "description": "Lorem Ipsum"
    }
    headers = {}
    response = requests.request("POST", url, headers=headers, json=payload)
    print(response.text.encode('utf8'))
    print(response.json().id)
    return HttpResponse(render(request, 'PagosTemplate/pagosDone.html',{'json': response.json()}))"""



"""  if request.method=='GET':
        listTrans=TransferenciaActual.objects.filter(cliente=request.user)
        #aki hay q mostrar todas las transferencias q el usuario a metido en el carrito
        return HttpResponse(render(request,'PagosTemplate/pagosGeneral.html',{'ListTrans':listTrans}))
    else:
        # vamos asuponer q pague: ahora hay q hacer todad las transferencias q haya hecho ese usuario
        listTrans = TransferenciaActual.objects.filter(cliente=request.user)
        JsonCubacel = ServerManage(listTrans)
        error = False
        for trans in JsonCubacel:
            if 'Error' in trans.__str__():
                error=True
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
"""

def procesarPago(request):
    return HttpResponse(render(request, 'PagosTemplate/pagosDone.html'))

