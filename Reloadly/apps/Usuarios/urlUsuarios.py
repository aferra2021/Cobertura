from django.conf.urls import url,include
from .views import Registrarse,Logout,adminUser,userExist,emailExist,ajax_posting_register,cantTransfer,nuevaRecarga,\
    ajax_login,GetEmail,GetUser,Comentar,ajax_Logout, carrito_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns=[
    url('registrar', Registrarse.as_view(), name='registrar'),
    url('iniciarsecion',ajax_login,name='iniciarsecion'),
    #url('iniciarsecion',auth_views.LoginView.as_view(),name='iniciarsecion'),
    url('cerrar/sesion', login_required(ajax_Logout), name='cerrar-sesion'),
    url('cerrar-sesion', login_required(Logout.as_view()), name='cerrar/sesion'),
    url('admin', login_required(adminUser), name='adminUser'),
    url('user', userExist, name='userExist'),
    url('GetEmail', GetEmail, name='GetEmail'),
    url('GetUser', GetUser, name='GetUser'),
    url('email', emailExist, name='emailExist'),
    url('ajax-posting/', ajax_posting_register, name='ajax_posting'),
    url(r'^cantidadtransferencia/',login_required(cantTransfer), name='cantidadtransferencia'),
    url(r'^nuevarecarga/', login_required(nuevaRecarga), name='nuevarecarga'),
    url(r'^carrito/', carrito_view, name='carrito'),
    #url(r'^comentar/(?P<slug>.*)$', login_required(Comentar), name='comentar'),
    url('comentar/',Comentar, name='comentar'),
   # url('comentar/(?P<result>\w+?)/$',Comentar2, name='comentar'),

]

