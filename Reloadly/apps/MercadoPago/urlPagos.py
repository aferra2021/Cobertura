from django.conf.urls import url,include
from apps.MercadoPago.views import pagosGeneral,procesarPago

urlpatterns=[
url(r'^targetas/', pagosGeneral, name='pago'),
#url(r'^procesar_pago/', procesarPago, name='procesar_pago'),
]