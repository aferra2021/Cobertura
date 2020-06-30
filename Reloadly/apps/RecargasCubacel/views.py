from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template,Context
from apps.Usuarios.models import TransferenciaActual
import datetime
from django.contrib.auth.models import User

def recargaCubacelView(request):
    if request.method=='GET':
        return HttpResponse(render(request, 'RecargasCubacelTemplates/RecargasCubacel.html'))
    else:
        if request.user:
            tipo='Cubacel'
            fecha=datetime.datetime.now()
            #user=User.objects.get(username=request.user)
            user=request.user
            AccountNumber=request.POST['AccountNumber']
            SendValue=int(request.POST['Recarga'])
            Trans=TransferenciaActual(tipo=tipo,fecha=fecha,cliente=user,SendValue=SendValue,accountNumber=AccountNumber)
            Trans.save()
        return redirect('pago')#pago

def recargaCubacelView2(request,offset):
    if request.method=='GET':
        print(offset)
        return HttpResponse(render(request, 'RecargasCubacelTemplates/RecargasCubacel.html'))
    else:
        if request.user:
            tipo='Cubacel'
            fecha=datetime.datetime.now()
            #user=User.objects.get(username=request.user)
            user=request.user
            AccountNumber=request.POST['AccountNumber']
            SendValue=int(request.POST['Recarga'])
            Trans=TransferenciaActual(tipo=tipo,fecha=fecha,cliente=user,SendValue=SendValue,accountNumber=AccountNumber)
            Trans.save()
        return redirect('pago')#pago
