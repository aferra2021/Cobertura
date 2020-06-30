from django.conf.urls import url, include
from apps.CubacelTur.views import CubacelTur

urlpatterns = [
    url('cubaceltur', CubacelTur, name='cubaceltur'),
]
