from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
import requests
from requests.exceptions import ConnectionError

# Create your views here.
def CubacelTur(request):
    return HttpResponse(render(request, 'CubacelTurTemplates/CubaceTur.html'))
   # return HttpResponse(render(request,'CubacelTurTemplates/CubacelTur.html'))