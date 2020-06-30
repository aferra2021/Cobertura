from django.conf.urls import url,include
from apps.Usuarios.views import Registrarse,Logout,adminUser,userExist,emailExist,ajax_posting
from django.contrib.auth import views as auth_views

urlpatterns=[
    url('registrar', Registrarse.as_view(), name='registrar'),
    url('iniciarsecion',auth_views.LoginView.as_view(),name='iniciarsecion'),
    url('cerrar-sesion', Logout.as_view(), name='cerrar-sesion'),
    url('admin', adminUser, name='adminUser'),
    url('user', userExist, name='userExist'),
    url('email', emailExist, name='emailExist'),
    url('ajax-posting/', ajax_posting, name='ajax_posting')
]
