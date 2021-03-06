"""Reloadly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .views import  inicio,inicioEN,Blog,Blog2,ServerManage0,TerminosCondiciones,bad_request,\
    permission_denied,page_not_found,my_custom_error_view
from django.urls import reverse_lazy

from django.conf.urls import (handler400, handler403, handler404, handler500)
#from django.utils.six.moves.urllib.parse import urlparse,urlunparse
#from django.contrib.auth.views import #password_reset,password_reset_done,password_reset_confirm, password_reset_complete
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^cobertura/en', inicioEN,name='coberturaEN'),
    url(r'^cobertura/', inicio, name='cobertura'),
    url(r'^ServerManage/', ServerManage0, name='ServerManage'),

    url(r'^blog/', Blog, name='blog'),
    url(r'^blog/(?P<result>\w+?)/$', Blog2, name='blog'),
    #terminos y condiciones
    url(r'^terminosCondiciones/', TerminosCondiciones, name='terminosCondiciones'),

    #social
    #url(r'^social/',include('social_django.urls', namespace='social')),
    #url('', include('social.apps.django_app.urls', namespace='social')),#google
    #url(r'^api/login/', include('rest_social_auth.urls_session'),name='authFace'),
    # apps
    url(r'cubacel/', include('apps.RecargasCubacel.urlRecargasCubacel')),  # lo de app1 es suseptible al cambio
    url(r'nauta/', include('apps.RecargasNauta.urlRecargasNauta')),  # lo de app2 es suseptible al cambio
    url(r'lineaCubacel/', include('apps.CubacelSimTelefono.urlCubacelSimTelefono')),  # lo de app3 es suseptible al cambio
    url(r'app4/', include('apps.EtecsaTelefonoFijo.urlEtecsaTelefonoFijo')),  # lo de app4 es suseptible al cambio
    url(r'app5/', include('apps.CubacelTur.urlCubacelTur')),  # lo de app5 es suseptible al cambio
    url(r'usuarios/', include('apps.Usuarios.urlUsuarios')),  # lo de app5 es suseptible al cambio
    url(r'accounts/login/',auth_views.LoginView.as_view(template_name='registration/loginMensaje.html'),name="loginMensaje"),  # lo de app5 es suseptible al cambio

    url(r'pagos/',include('apps.StripeAPI.urlStripeAPI')),  # lo de stripe es suseptible al cambio
    #url(r'mercadopago/', include('apps.MercadoPago.urlPagos')),#PAGOS

#reset_password
    url('^', include('django.contrib.auth.urls')),
    url(
        r'^recuperar/contraseña/$',
        auth_views.PasswordResetView.as_view(
            template_name='auth/password_reset_form.html',
            html_email_template_name='auth/password_reset_email.html',
        ),
        name='password_recovery',
    ),
    url(
        r'^recuperacion/contraseña/completada/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='auth/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    url(
        r'^recuperacion/contraseña/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('password_reset_completo'),
            post_reset_login=True,
            template_name='auth/password_reset_confirm.html',
            post_reset_login_backend=(
                'django.contrib.auth.backends.AllowAllUsersModelBackend'
            ),
        ),
        name='password_reset_confirm',
    ),
    url(r'^contraseña/recuperada/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth/password_reset_complete.html'), name='password_reset_completo'),
]
handler400 = bad_request
handler403 = permission_denied
handler404 = page_not_found
handler500 = my_custom_error_view
