from django.conf.urls import url,include
from apps.Pagos.views import pagosGeneral

urlpatterns=[
url(r'^targetas/', pagosGeneral, name='pago'),
]