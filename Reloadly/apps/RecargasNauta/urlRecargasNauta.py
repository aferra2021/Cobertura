from django.conf.urls import url,include
from apps.RecargasNauta.views import RecargaNauta2

urlpatterns=[
    url('recarga/(\d{1,2})/$', RecargaNauta2, name='nauta'),
    #url('nauta', RecargaNauta,name='nauta'),
]