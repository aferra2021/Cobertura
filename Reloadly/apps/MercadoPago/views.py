from django.shortcuts import render
from apps.Usuarios.models import TransferenciaActual,TranferenciaGeneral,Contacto
from django.http import HttpResponse
from Reloadly.ServiciosGenerales import ServerManage
from django.contrib.auth.models import User
import requests
from .ServiciosMercadoPago import CrearClienteAPI,ObtenerCliente
from .models import ClienteMercadoPago

# Create your views here.
#access_token=TEST-3968442574725364-052821-0a162b8a21c4dbd43f48933d227339ce-468607165'

def pagosGeneral(request):
    #get en el q mando el formulario para llenar los datos del cliente de tarjeta
    #en el post recojo los datos
    url='https://api.mercadopago.com/v1/payments?access_token=TEST-3968442574725364-052821-0a162b8a21c4dbd43f48933d227339ce-468607165'
    url='https://api.mercadopago.com/v1/payments?access_token=TEST-3968442574725364-052821-0a162b8a21c4dbd43f48933d227339ce-468607165'
   # // api.mercadopago.com / v1 / customers / {} / cards
    #payload={            }
    headers = {}
    #response = requests.request("POST", url, headers=headers, json=payload)
    response=CrearClienteAPI()
    response = requests.request("GET", 'https://api.mercadopago.com/v1/customers/606370491-Q5eBJUglok98pa/cards?access_token=TEST-3968442574725364-052821-0a162b8a21c4dbd43f48933d227339ce-468607165', headers=headers, json={})

    #id=606370491-Q5eBJUglok98pa
    return HttpResponse(render(request, 'PagosTemplate/pagosDone.html', {'ClienteMercadoPago': response.json()}))







    """CC=CrearClienteAPI()
    if CC['error']=='':#no hubo error
        ClienteMercadoPago=ModeloClenteMercadoPago(CC)
        ClienteMercadoPago.save()
        return HttpResponse(render(request, 'PagosTemplate/pagosDone.html',{'ClienteMercadoPago':ClienteMercadoPago}))"""
    #if CC['error']
    #tengo q renderizar el formulario denuevo y mostrarle al usuario el error del campo en el que se equivoco


def CrearClienteMercadoPago(request):
    ListTrans=TransferenciaActual.objects.filter(cliente=request.user)
    return HttpResponse(render(request, 'PagosTemplate/crearClienteMercadoPago.html',{'ListTrans':ListTrans}))


"""  if request.method=='GET':
        listTrans=TransferenciaActual.objects.filter(cliente=request.user)
        #aki hay q mostrar todas las transferencias q el usuario a metido en el carrito
        return HttpResponse(render(request,'PagosTemplate/crearClienteMercadoPago.html',{'ListTrans':listTrans}))
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

def ModeloClenteMercadoPago(response_json):
    id = response_json['id']
    email = response_json['email']
    first_name = response_json['first_name']
    last_name = response_json['last_name']
    # phone
    area_Code = response_json['phone']['area_code']
    number = response_json['phone']['number']
    # identification
    type = response_json['identification']['type']
    numberIdentifications = response_json['identification']['number']
    date_created = response_json['date_created']
    date_last_updated = response_json['date_last_updated']
    CMP = ClienteMercadoPago(id=id, email=email, first_name=first_name,last_name=last_name, area_Code=area_Code, number=number,type=type, numberIdentifications=numberIdentifications,date_created=date_created,date_last_updated=date_last_updated)
    return CMP