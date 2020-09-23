from django.conf.urls import url,include
from .views import RecargaNauta,Test

urlpatterns=[
    url('recarga/test', Test, name='nautaTest'),
    url('recarga/nauta/([1-9][n])/([\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4})/([a-zA-Z0-9]{0,200})$', RecargaNauta, name='nauta'),

    #url('nauta', RecargaNauta,name='nauta'),
]