from django.contrib import admin
from .models import TranferenciaGeneral,TransferenciaActual,Contacto,Comentario,ReservasHechas
# Register your models here.
admin.site.register(TranferenciaGeneral)
admin.site.register(TransferenciaActual)
admin.site.register(Contacto)
admin.site.register(Comentario)
admin.site.register(ReservasHechas)
