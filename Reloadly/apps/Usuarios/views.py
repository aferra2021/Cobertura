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
from .models import TransferenciaActual,Comentario
import datetime

# Create your views here.
from json.decoder import JSONArray
import sweetify
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
        return redirect('cobertura')

def ajax_posting_register(request):
    if request.is_ajax():
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        usuario = User.objects.create_user(username=username, password=password, email=email)
        usuario.save()
        user = authenticate(username=username, password=password)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return JsonResponse({'Result':'True'})

def ajax_login(request):
    if request.is_ajax():
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return JsonResponse({'Result':'True'})
        else:
            return JsonResponse({'Result':'False'})
    return HttpResponse(render(request,'registration/login.html'))

class Logout(LogoutView):
    pass

def ajax_Logout(request):
    print('llego')
    print('llego')
    print('llego')
    print('llego')
    listTrans = TransferenciaActual.objects.filter(cliente=request.user)
    for trans in listTrans:
        trans.delete()
    return redirect('cerrar/sesion')

def GetUser(request):
    return JsonResponse({'Result':request.user.__str__()})

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

def GetEmail(request):
    user=request.GET['user']
    email=User.objects.get(username=user).email
    if email:
         return JsonResponse({'email':email})
    else:
        return JsonResponse({'email':None})

"""def Comentar2(request,result):
    user = request.user
    Comm = Comentario.objects.get(id=result)
    Comm.user = user
    Comm.save()
    return redirect('blog')"""

def Comentar(request):
    if request.is_ajax():
        comment='text' in request.POST
        comment=request.GET['text']
        if request.user.is_authenticated:
            user=request.user
            comentario=Comentario(user=user,text=comment,created=datetime.datetime.now())
            comentario.save()
            return JsonResponse({'Result':True})
        else:
            comentario=Comentario(text=comment,user=None,created=datetime.datetime.now())
            comentario.save()
            return JsonResponse({'Result':False,'id':comentario.id})
    comentarios=Comentario.objects.all()
    for coment in comentarios:
        print(coment)
    if request.user.is_authenticated:
        Carrito=TransferenciaActual.objects.filter(cliente=request.user)
        return HttpResponse(render(request,'UsuariosTemplates/blog.html',{'carrito':len(Carrito),'comentarios':comentarios}))
    return HttpResponse(render(request,'UsuariosTemplates/blog.html',{'carrito':0,'comentarios':comentarios}))

"""
def Comentar(request):
    if request.is_ajax():
        comment='text' in request.POST
        print(comment)
        print(comment)
        print(comment)
        print(comment)
        print(comment)
        comment=request.GET['text']
        if request.user.is_authenticated:
            user=request.user
            comentario=Comentario(user=user,text=comment,created=datetime.datetime.now())
        else:
            comentario=Comentario(user=None,text=comment,created=datetime.datetime.now())
        comentario.save()
        if comentario:
            return JsonResponse({'Result':True})
        else:
            return JsonResponse({'Result':False})
    return HttpResponse(render(request, 'UsuariosTemplates/blog.html'))
"""
"""user=request.user
    Trans=TransferenciaActual.objects.get(id=result)
    Trans.cliente = user
    Trans.save()"""


def adminUser(request):
    if request.method=='POST':
        pass
    else:
        return HttpResponse(render(request, 'UsuariosTemplates/userAdmin.html'))
#admin de usuario

def cantTransfer(request):
    if request.method == 'POST':
        pass
    else:
        return HttpResponse(render(request, 'UsuariosTemplates/cantTransfer.html'))

def nuevaRecarga(request):
    if request.method == 'POST':
        pass
    else:
        return HttpResponse(render(request, 'UsuariosTemplates/nuevaRecarga.html'))

def carrito_view(request):
    if request.user.is_authenticated:
        Carrito = TransferenciaActual.objects.filter(cliente=request.user)
        return HttpResponse(render(request, 'UsuariosTemplates/carrito.html', {'carrito': len(Carrito)}))
    return HttpResponse(render(request, 'UsuariosTemplates/carrito.html',{'carrito': 0}))
