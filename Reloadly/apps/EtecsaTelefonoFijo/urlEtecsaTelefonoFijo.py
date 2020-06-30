from django.conf.urls import url,include
from apps.EtecsaTelefonoFijo.views import EtecsaTelefonoFijo

urlpatterns=[
    url('etecsa', EtecsaTelefonoFijo,name='etecsa'),
]