import json
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.template import Template,Context
from apps.Usuarios.models import TransferenciaActual,Contacto
import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from apps.ServiciosDing.Servicios import PromocionesPorOperadorId,FechaFormat,PresioDeRecargaPorIdDeOferta

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
            Trans=TransferenciaActual(tipo=tipo,Descripcion='esta es una recarga de blablabla',fecha=fecha,cliente=user,SendValue=SendValue,accountNumber=AccountNumber)
            Trans.save()
        return redirect('pago')#pago

def recargaCubacelDefault(request,offset,offset2,contact):
   #try:
        contacto = None
        if not contact == '':
            if request.user.is_authenticated:
                try:
                    contactos = Contacto.objects.get(name=contact, user=request.user)
                except:
                    contactos = None

                if not contactos:
                    contacto = Contacto(name=contact.__str__(), accountNumber="53".__str__()+offset2.__str__(), user=request.user)
                    contacto.save()
                else:
                    contacto = contactos
            else:
                contacto = Contacto(name=contact.__str__(),accountNumber="53".__str__()+offset2.__str__())
                contacto.save()
            AccountNumber = offset2.__str__()
        else:
            AccountNumber = offset2.__str__()
        tipo='Recarga Cubacel'
        fecha=datetime.datetime.now()
        SendValue=PresioDeRecargaPorIdDeOferta(offset)
        presioBase=SendValue/int(offset[0])#aki hay q hacer lo de las orfertas
        descripción ="BLABAlabalanalabaallalaLA de "+ presioBase.__str__()+" blabalbalbalbalbalaba"
        cant=int(offset[0])
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            Trans=TransferenciaActual(tipo=tipo,Descripcion=descripción,fecha=fecha,cliente=user,SendValue=SendValue,
                                      accountNumber=AccountNumber,cant=cant,contacto=contacto)
            Trans.save()
            return redirect(reverse('carrito'))
        else:
            Trans=TransferenciaActual(tipo=tipo,Descripcion=descripción,fecha=fecha,cliente=None,SendValue=SendValue,
                                      accountNumber=AccountNumber,cant=cant,contacto=contacto)
            Trans.save()
            result=Trans.id
            return redirect(reverse('pagoStripeAPI', kwargs={'result': result}))
   #except:
   #    return redirect(reverse('cobertura'))

def recargaCubacelReserva(request,offset,offset2,contact):
    try:
        contacto = None
        if not contact == '':
            if request.user.is_authenticated:
                try:
                    contactos = Contacto.objects.get(name=contact, user=request.user)
                except:
                    contactos = None
                if not contactos:
                    contacto = Contacto(name=contact.__str__(), accountNumber="53".__str__()+offset2.__str__(), user=request.user)
                    contacto.save()
                else:
                    contacto = contactos
            else:
                contacto = Contacto(name=contact.__str__(),accountNumber="53".__str__()+offset2.__str__())
                contacto.save()
            AccountNumber = offset2.__str__()
        else:
            AccountNumber = offset2.__str__()
        cubacelPromotion=PromocionesPorOperadorId(103)[0]
        tipo = 'Reserva Saldo+Bono'
        fecha = datetime.datetime.now()
        SendValue = PresioDeRecargaPorIdDeOferta(offset)
        presioBase = SendValue / int(offset[0])  # aki hay q hacer lo de las orfertas
        descripción = cubacelPromotion['description']
        cant = int(offset[0])
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            Trans = TransferenciaActual(tipo=tipo, Descripcion=descripción, fecha=fecha, cliente=user,
                                        SendValue=SendValue, accountNumber=AccountNumber,cant=cant,contacto=contacto)
            Trans.save()
            return redirect(reverse('carrito'))
        else:
            Trans = TransferenciaActual(tipo=tipo, Descripcion=descripción, fecha=fecha, cliente=None,
                                        SendValue=SendValue, accountNumber=AccountNumber,cant=cant,contacto=contacto)
            Trans.save()
            result = Trans.id
            return redirect(reverse('pagoStripeAPI', kwargs={'result': result}))
    except:
        return redirect(reverse('cobertura'))

def recargaCubacelBono(request,offset,offset2,contact):
    try:
        contacto = None
        if not contact == '':
            if request.user.is_authenticated:
                try:
                    contactos = Contacto.objects.get(name=contact, user=request.user)
                except:
                    contactos = None
                if not contactos:
                    contacto = Contacto(name=contact.__str__(), accountNumber="53".__str__()+offset2.__str__(), user=request.user)
                    contacto.save()
                else:
                    contacto = contactos
            else:
                contacto = Contacto(name=contact.__str__(), accountNumber="53".__str__()+offset2.__str__())
                contacto.save()
            AccountNumber = offset2.__str__()
        else:
            AccountNumber = offset2.__str__()
        cubacelPromotion=PromocionesPorOperadorId(103)[0]
        tipo = 'Saldo+Bono'
        fecha = datetime.datetime.now()
        SendValue = PresioDeRecargaPorIdDeOferta(offset)
        presioBase = SendValue / int(offset[0])  # aki hay q hacer lo de las orfertas
        descripción = "titulo"
        cant = int(offset[0])
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            Trans = TransferenciaActual(tipo=tipo, Descripcion=descripción, fecha=fecha, cliente=user,SendValue=SendValue,
                                        accountNumber=AccountNumber,cant=cant,contacto=contacto)
            Trans.save()
            return redirect(reverse('carrito'))
        else:
            Trans = TransferenciaActual(tipo=tipo, Descripcion=descripción, fecha=fecha, cliente=None,SendValue=SendValue,
                                        accountNumber=AccountNumber,cant=cant,contacto=contacto)
            Trans.save()
            result = Trans.id
            return redirect(reverse('pagoStripeAPI', kwargs={'result': result}))
    except:
        return redirect(reverse('cobertura'))

def recargaCubacelPaquetes(request,offset,offset2,contact):
    try:
        contacto = None
        if not contact == '':
            if request.user.is_authenticated:
                try:
                    contactos = Contacto.objects.get(name=contact, user=request.user)
                except:
                    contactos = None
                if not contactos:
                    contacto = Contacto(name=contact.__str__(), accountNumber="53".__str__()+offset2.__str__(), user=request.user)
                    contacto.save()
                else:
                    contacto = contactos
            else:
                contacto = Contacto(name=contact.__str__(), accountNumber="53".__str__()+offset2.__str__())
                contacto.save()
            AccountNumber = offset2.__str__()
        else:
            AccountNumber = offset2.__str__()
        #cubacelPromotion = PromocionesPorOperadorId(103)[0]
        tipo = 'Datos Moviles Cubacel'
        fecha = datetime.datetime.now()
        SendValue = PresioPaquetes(int(offset[0]))
        descripción = Description(int(offset[0]))
        cant = int(offset[0])
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            Trans = TransferenciaActual(tipo=tipo, Descripcion=descripción, fecha=fecha, cliente=user,
                                        SendValue=SendValue, accountNumber=AccountNumber,cant=cant,contacto=contacto)
            Trans.save()
            return redirect(reverse('carrito'))
        else:
            Trans = TransferenciaActual(tipo=tipo, Descripcion=descripción, fecha=fecha, cliente=None,
                                        SendValue=SendValue, accountNumber=AccountNumber,cant=cant,contacto=contacto)
            Trans.save()
            result = Trans.id
            return redirect(reverse('pagoStripeAPI', kwargs={'result': result}))
    except:
        return redirect(reverse('cobertura'))

def ajax_promotion_cubacel(request):
    try:
        cubacelPromotion=PromocionesPorOperadorId(103)
        if cubacelPromotion!=[]:
            PromotionId=cubacelPromotion[0]['promotionId']
            OperadorId=cubacelPromotion[0]['operatorId']
            title1=cubacelPromotion[0]['title']
            title2=cubacelPromotion[0]['title2']
            descripción =cubacelPromotion[0]['description']
            StartDate=FechaFormat(cubacelPromotion[0]['startDate'])
            endDate=FechaFormat(cubacelPromotion[0]['endDate'])
            if StartDate > datetime.datetime.now():
                #reserva
                return JsonResponse({'Empty':True,'Time':'before','promotionId':PromotionId,'operadorId':OperadorId,'title1':title1,'title2':title2,"descripción":descripción,'Fecha':StartDate})
            else:
                if endDate>datetime.datetime.now():
                    #promo normal
                    return JsonResponse({'Empty':True,'Time':'after','promotionId':PromotionId,'operadorId':OperadorId,'title1':title1,'title2':title2,"descripción":descripción,'Fecha':StartDate})
        else:
            return JsonResponse({'Empty': False})
        return JsonResponse({'Empty': False})
    except:
        return JsonResponse({'Empty': False})

#hay q hacerun triyer
def Description(off):
    description=''
    if off==1:
        description='Paquete de 600 MB'
    elif off==2:
        description='Paquete de 600 MB por LTE (4G)'
    elif off==3:
        description = 'Paquete de 1 GB'
    elif off==4:
            description='Paquete de 1 GB por LTE (4G)'
    elif off==5:
            description='Paquete de 2.5 GB, uso en todas las frecuencias 3G y 4G'
    elif off==6:
            description='Paquete de 4 GB, uso en todas las frecuencias 3G y 4G'
    return  description

def PresioPaquetes(off):
    presio = 0
    if off == 1:
        presio = 7
    elif off == 2:
        presio = 7
    elif off == 3:
        presio = 10
    elif off == 4:
        presio = 10
    elif off == 5:
        presio = 20
    elif off == 6:
        presio = 30
    return presio