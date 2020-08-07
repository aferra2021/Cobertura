from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.template import Template,Context
from apps.Usuarios.models import TransferenciaActual
import datetime
from django.contrib.auth.models import User

def recargaCubacelView(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            Carrito = TransferenciaActual.objects.filter(cliente=request.user)
            return HttpResponse(render(request, 'RecargasCubacelTemplates/RecargasCubacel.html', {'carrito': len(Carrito)}))
        return HttpResponse(render(request, 'RecargasCubacelTemplates/RecargasCubacel.html', {'carrito': 0}))
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
        #offset es para controlar q oferta de recarga se pidio
        if request.user.is_authenticated:
            Carrito = TransferenciaActual.objects.filter(cliente=request.user)
            return HttpResponse(render(request, 'RecargasCubacelTemplates/RecargasCubacel.html', {'carrito': len(Carrito)}))
        return HttpResponse(render(request, 'RecargasCubacelTemplates/RecargasCubacel.html', {'carrito': 0}))
    else:
        tipo='Cubacel'
        fecha=datetime.datetime.now()
        AccountNumber=request.POST['AccountNumber']
        SendValue=int(request.POST['Recarga'])
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            Trans=TransferenciaActual(tipo=tipo,fecha=fecha,cliente=user,SendValue=SendValue,accountNumber=AccountNumber)
            Trans.save()
            return redirect(reverse('pagoStripeAPI'))
        else:
            Trans=TransferenciaActual(tipo=tipo,fecha=fecha,cliente=None,SendValue=SendValue,accountNumber=AccountNumber)
            Trans.save()
            result=Trans.id
            return redirect(reverse('pagoStripeAPI', kwargs={'result': result}))
