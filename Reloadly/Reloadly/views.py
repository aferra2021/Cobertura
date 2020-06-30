from json.decoder import JSONArray

from django.template import Template,Context
from django.http import HttpResponse,Http404
from django.shortcuts import render
from apps.Usuarios.models import TransferenciaActual
from .ServiciosGenerales import ServerManage
from django.template import RequestContext
from rest_social_auth.views import SocialSessionAuthView
from .serializers import MyUserSerializer

def inicio(request):
    return HttpResponse(render(request,'index.html'))
def inicioEN(request):
    return HttpResponse(render(request,'indexEn.html'))

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
        return HttpResponse(render(request, 'PagosTemplate/pagosDone.html',{'json':JsonCubacel}))

def nuevaRecarga(request):
    pass

class MySocialView(SocialSessionAuthView):
      serializer_class = MyUserSerializer


########################################################################################################################
def bad_request(request,exception):#400
    response = HttpResponse(render(request,'ExceptionTemplates/400.html'))
    response.status_code = 400
    return response

def permission_denied(request,exception):#403
    response = HttpResponse(render(request,'ExceptionTemplates/403.html'))
    response.status_code = 403
    return response

def page_not_found(request,exception):#404
    response = HttpResponse(render(request,'ExceptionTemplates/404.html'))
    response.status_code = 404
    return response

def my_custom_error_view(request):#500
    response = HttpResponse(render(request,'ExceptionTemplates/500.html'))
    response.status_code = 500
    return response


