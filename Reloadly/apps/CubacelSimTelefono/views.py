from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
import requests
from requests.exceptions import ConnectionError
from apps.Usuarios.models import TransferenciaActual

# Create your views here.
def CubacelSimTelefono(request):
    if request.user.is_authenticated:
        Carrito=TransferenciaActual.objects.filter(cliente=request.user)
        return HttpResponse(render(request,'CubacelSimTelefonoTemplates/CubacelSimTelefono.html',{'cantidadCarrito':len(Carrito)}))
    return HttpResponse(render(request,'CubacelSimTelefonoTemplates/CubacelSimTelefono.html',{'cantidadCarrito':0,}))

