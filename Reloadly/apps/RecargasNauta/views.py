from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from apps.Usuarios.models import TransferenciaActual
from django.template import Template,Context
from requests.exceptions import ConnectionError

# Create your views here.

def RecargaNauta2(request,offset):
    if request.method=='GET':
        print(offset)
        return HttpResponse(render(request, 'RecargasNautaTemplates/RecargasNauta.html'))
    else:
        if request.user:
            tipo='Nauta'
            fecha=datetime.datetime.now()
            #user=User.objects.get(username=request.user)
            user=request.user
            AccountNumber=request.POST['AccountNumber']
            SendValue=int(request.POST['Recarga'])
            Trans=TransferenciaActual(tipo=tipo,fecha=fecha,cliente=user,SendValue=SendValue,accountNumber=AccountNumber)
            Trans.save()
        return redirect('pago')#pago

def RecargaNauta(request):
    return HttpResponse(render(request,'RecargasNautaTemplates/RecargasNauta.html'))