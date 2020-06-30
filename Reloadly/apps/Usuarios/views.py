from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate
from django.contrib.auth import login as do_login
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .formRegistro import RegistroFormUsuario
# Create your views here.
from json.decoder import JSONArray

class Registrarse(CreateView):
    model = User
    form_class = RegistroFormUsuario

    def form_valid(self, form_class):

        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el
        usuario inicie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form_class.save()
        username = form_class.cleaned_data.get('username')
        password = form_class.cleaned_data.get('password1')
        email = form_class.cleaned_data.get('email')
        usuario = authenticate(username=username, password=password,email=email)
        login(self.request, usuario)
        return redirect('reloadlycuba')

def ajax_posting(request):
    if request.is_ajax():
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        usuario = User.objects.create_user(username=username, password=password, email=email)
        usuario.save()
        user = authenticate(username=username, password=password)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return JsonResponse({'Result':'True'})



def userExist(request):
    userNameReg=request.GET['user']
    user = User.objects.filter(username=userNameReg)
    if user:
        return JsonResponse({'Result': 'True'})
    else:
       return JsonResponse({'Result': 'False'})

def emailExist(request):
    emailForm=request.GET['email']
    email = User.objects.filter(email=emailForm)
    if email:
        return JsonResponse({'Result': 'True'})
    else:
       return JsonResponse({'Result': 'False'})


class Logout(LogoutView):
    pass

def adminUser(request):
    if request.method=='POST':
        pass
    else:
        return HttpResponse(render(request, 'UsuariosTemplates/userAdmin.html'))
#admin de usuario

