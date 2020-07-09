from django.conf.urls import url,include
from apps.MercadoPago.views import pagosGeneral,procesarPago,CrearClienteMercadoPago

urlpatterns=[
url(r'^clientePago/', CrearClienteMercadoPago, name='crearClienteMercadoPago'),
url(r'^tarjetas/', pagosGeneral, name='pago'),
#url(r'^procesar_pago/', procesarPago, name='procesar_pago'),
]