from json.decoder import JSONArray
from django.template import Template,Context
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect,reverse
from django.template import RequestContext
from django.views.generic import UpdateView
from .serializers import MyUserSerializer
from django.contrib.auth.models import User
from apps.Usuarios.models import Comentario,TransferenciaActual
from apps.RecargasCubacel.views import ajax_promotion_cubacel
from .ServiciosGenerales import ServerManage

def ServerManage0(request):
   return ServerManage(request)

def inicio(request):
    if request.user.is_authenticated:
        Carrito=TransferenciaActual.objects.filter(cliente=request.user)
        return HttpResponse(render(request,'index.html',{'cantidadCarrito':len(Carrito),'bool':'false','Promotion':ajax_promotion_cubacel}))
    return HttpResponse(render(request,'index.html',{'cantidadCarrito':0,'bool':'false','Promotion':ajax_promotion_cubacel}))

def inicioEN(request):
    if request.user.is_authenticated:
        Carrito=TransferenciaActual.objects.filter(cliente=request.user)
        return HttpResponse(render(request,'indexEn.html',{'cantidadCarrito':len(Carrito),'bool':'false','Promotion':ajax_promotion_cubacel}))
    return HttpResponse(render(request,'indexEn.html',{'cantidadCarrito':0,'bool':'false','Promotion':ajax_promotion_cubacel}))

def Blog2(request,result):
    user = request.user
    Comm = Comentario.objects.get(id=result)
    Comm.user = user
    Comm.save()
    return redirect('blog')

def Blog(request):
    return redirect('comentar')


def TerminosCondiciones(request):
    response = HttpResponse(render(request,'UsuariosTemplates/terminosCondiciones.html'))
    return response


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
