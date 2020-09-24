from django.conf.urls import url,include
from apps.CubacelSimTelefono.views import CubacelSimTelefono

urlpatterns=[
    url('', CubacelSimTelefono,name='cubacelventa'),
]