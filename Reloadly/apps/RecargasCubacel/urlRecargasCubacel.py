from django.conf.urls import url,include
from .views import recargaCubacelView,recargaCubacelDefault,recargaCubacelReserva,recargaCubacelBono,ajax_promotion_cubacel,recargaCubacelPaquetes

urlpatterns=[
    #[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}
    url('recarga/cubacel/([1-9][d])/([5][0123456789]{1,8})/([a-zA-Z0-9]{0,200})$', recargaCubacelDefault,name='cubacelDefault'),
    url('recarga/reserva/([1-9][r])/([5][0123456789]{1,8})/([a-zA-Z0-9]{0,200})$', recargaCubacelReserva,name='cubacelReserva'),
    url('recarga/bono/([1-9][b])/([5][0123456789]{1,8})/([a-zA-Z0-9]{0,200})$', recargaCubacelBono,name='cubacelBono'),
    url('recarga/paquetes/([1-9][p])/([5][0123456789]{1,8})/([a-zA-Z0-9]{0,200})$', recargaCubacelPaquetes,name='recargaCubacelPaquetes'),
    url('ajax_promotion_cubacel', ajax_promotion_cubacel,name='ajax_promotion_cubacel'),
  #  url('recarga', recargaCubacelView, name='cubacel'),
]

