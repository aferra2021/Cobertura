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
from .models import TransferenciaActual,Comentario,Contacto
import datetime
from django.forms.models import model_to_dict
import json

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
        return JsonResponse({'Result':'True','usuario':user.__str__()})

def ajax_login(request):
    if request.is_ajax():
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return JsonResponse({'Result':'True','usuario':user.__str__()})
        else:
            return JsonResponse({'Result':'False'})
    if request.user.is_authenticated:
        Carrito = TransferenciaActual.objects.filter(cliente=request.user)
        return HttpResponse(render(request,'registration/login.html',{'cantidadCarrito': len(Carrito)}))
    return HttpResponse(render(request,'registration/login.html',{'cantidadCarrito':0}))

class Logout(LogoutView):
    pass

def ajax_Logout(request):
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

def Comentar(request):
    if request.is_ajax():
        comment='text' in request.POST
        comment=request.GET['text']
        if request.user.is_authenticated:
            user=request.user
            comentario=Comentario(user=user,text=comment,created=datetime.datetime.now(),votosP=0,votosN=0)
            comentario.save()
            return JsonResponse({'Result':True})
        else:
            comentario=Comentario(text=comment,user=None,created=datetime.datetime.now(),votosP=0,votosN=0)
            comentario.save()
            return JsonResponse({'Result':False,'id':comentario.id})
    comentarios=Comentario.objects.all()
    if request.user.is_authenticated:
        #Carrito=reversed(Carrito)
        Carrito=TransferenciaActual.objects.filter(cliente=request.user)
        return HttpResponse(render(request,'UsuariosTemplates/blog.html',{'cantidadCarrito':len(Carrito),'comentarios':comentarios}))
    return HttpResponse(render(request,'UsuariosTemplates/blog.html',{'cantidadCarrito':0,'comentarios':comentarios}))

def AjaxLikeComment(request):
    id=request.GET['id']
    like=request.GET['like']
    Sentido=int(request.GET['direction'])
    disminuir=request.GET['disminuir']
    comment=Comentario.objects.get(id=id)
    if like=='like':
        comment.votosP=comment.votosP+Sentido
    else:
        comment.votosN=comment.votosN+Sentido

    if disminuir=='like':
        comment.votosP = comment.votosP -1
    if disminuir=='dislike':
        comment.votosN = comment.votosN -1
    comment.save()
    return JsonResponse({'Result':True})

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

def carrito_view(request):
    Carrito = TransferenciaActual.objects.filter(cliente=request.user)
    if request.user.is_authenticated:
        return HttpResponse(render(request, 'UsuariosTemplates/carrito.html', {'cantidadCarrito': len(Carrito),'carrito':Carrito}))
    return HttpResponse(render(request, 'UsuariosTemplates/carrito.html',{'cantidadCarrito': 0,'carrito':Carrito}))


def carritoAside(request):
    Carrito = TransferenciaActual.objects.filter(cliente=request.user)
    if request.user.is_authenticated:
        return HttpResponse(render(request, 'UsuariosTemplates/carritoAside.html', {'cantidadCarrito': len(Carrito),'carrito':Carrito}))
    return HttpResponse(render(request, 'UsuariosTemplates/carritoAside.html',{'cantidadCarrito': 0,'carrito':Carrito}))



from django.core import serializers
def ajax_carrito(request):
    cliente=User.objects.get(username=request.GET['user'])
    Carrito=TransferenciaActual.objects.filter(cliente=cliente.pk)
    if len(Carrito)>0:
        return JsonResponse({"Carrito":True,'len':len(Carrito)})

    return JsonResponse({"Carrito": False})

def ajax_Carrito_serializer(request):
    id=request.GET['id']
    try:
        cliente=User.objects.get(username=request.GET['user'])
        Carrito=TransferenciaActual.objects.filter(cliente=cliente.pk)[int(id)]
        data = serializers.serialize('json', [Carrito, ])
        struct = json.loads(data)
        data = json.dumps(struct[0])
        contacto=Carrito.contacto
        if contacto:
            return JsonResponse({'Result':data,'boolContact':True,'contactoName':contacto.name,'bool':True})
        return JsonResponse({'Result':data,'boolContact':False,'bool':True})
    except:
        return JsonResponse({'bool':False})

def get_contactos_cubacel(request):
    usuario = User.objects.get(username=request.GET['user'])

    contactos=Contacto.objects.filter(user=usuario.pk)
    data=[]
    data2=[]
    c=0
    for i in contactos:
        if not i.accountNumber.__str__()[   len(i.accountNumber)-1]=='u':
            data.append(i.name)
            data2.append(i.accountNumber)
        c=c+1
    if data:
        return JsonResponse({'Result': data,'Result2':data2, 'bool': True})
    return JsonResponse({'bool': False})

def get_contactos_nauta(request):
    usuario = User.objects.get(username=request.GET['user'])

    contactos=Contacto.objects.filter(user=usuario.pk)
    data=[]
    data2=[]
    c=0
    for i in contactos:
        if i.accountNumber.__str__()[   len(i.accountNumber)-1]=='u':
            data.append(i.name)
            data2.append(i.accountNumber)
        c=c+1
    if data:
        return JsonResponse({'Result': data,'Result2':data2, 'bool': True})
    return JsonResponse({'bool': False})


"""def nuevaRecarga(request):
    if request.method == 'POST':
        pass
    else:
        return HttpResponse(render(request, 'UsuariosTemplates/nuevaRecarga.html'))"""

def EliminarRecarga(request):
    id=request.GET['id']
    trans=TransferenciaActual.objects.filter(pk=id)
    trans.delete()
    return JsonResponse({'Result':True})

