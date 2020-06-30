from django.conf.urls import url,include
from apps.RecargasCubacel.views import recargaCubacelView,recargaCubacelView2

urlpatterns=[
    url('recarga/(\d{1,2})/$', recargaCubacelView2,name='cubacel'),
  #  url('recarga', recargaCubacelView, name='cubacel'),

]