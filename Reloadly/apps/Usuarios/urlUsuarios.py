from django.conf.urls import url,include
from .views import Registrarse,Logout,adminUser,userExist,emailExist,ajax_posting_register,cantTransfer,\
    ajax_login,GetEmail,GetUser,Comentar,ajax_Logout, carrito_view,carritoAside,AjaxLikeComment,EliminarRecarga,ajax_carrito,\
    ajax_Carrito_serializer,get_contactos_cubacel,get_contactos_nauta
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns=[
    url('registrar', Registrarse.as_view(), name='registrar'),
    url('iniciarsecion',ajax_login,name='iniciarsecion'),
    #url('iniciarsecion',auth_views.LoginView.as_view(),name='iniciarsecion'),
    url('cerrar/sesion', login_required(ajax_Logout), name='cerrar-sesion'),
    url('cerrar-sesion', login_required(Logout.as_view()), name='cerrar/sesion'),
    url('admin', login_required(adminUser), name='adminUser'),
    #url('nuevaRecarga', login_required(nuevaRecarga), name='nuevaRecarga'),
    url('user', userExist, name='userExist'),
    url('GetEmail', GetEmail, name='GetEmail'),
    url('GetUser', GetUser, name='GetUser'),
    url('email', emailExist, name='emailExist'),
    url('ajax-posting/', ajax_posting_register, name='ajax_posting'),
    url(r'^cantidadtransferencia/',login_required(cantTransfer), name='cantidadtransferencia'),
    url(r'^carrito/', login_required(carrito_view), name='carrito'),
    url(r'^carritoAside/', login_required(carritoAside), name='carritoAside'),
    #url(r'^comentar/(?P<slug>.*)$', login_required(Comentar), name='comentar'),
    url('comentar/',Comentar, name='comentar'),
    url('ajax_likeComment/',AjaxLikeComment, name='AjaxLikeComment'),
    url('eliminar_recarga/',EliminarRecarga, name='EliminarRecarga'),
    url('ajax_carrito/',ajax_carrito, name='ajax_carrito'),
    url('ajax_Carrito_serializer/',ajax_Carrito_serializer, name='ajax_Carrito_serializer'),
    url('get_contactos_cubacel/',get_contactos_cubacel, name='get_contactos_cubacel'),
    url('get_contactos_nauta/',get_contactos_nauta, name='get_contactos_nauta'),
   # url('comentar/(?P<result>\w+?)/$',Comentar2, name='comentar'),

]

