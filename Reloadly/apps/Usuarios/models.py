from django.db import models
from django.contrib.auth.models import User
from apps.MercadoPago.models import ClienteMercadoPago
# Create your models here.


class Contacto(models.Model):
    user = models.ManyToManyField(User)
    accountNumber=models.IntegerField()

class TranferenciaGeneral(models.Model):
    tipo=models.CharField(max_length=50)
    fecha=models.DateTimeField()
    cliente=models.ForeignKey(User,on_delete=models.CASCADE)
    SendValue=models.IntegerField()
    contacto=models.ForeignKey(Contacto,on_delete=models.PROTECT)
    clienteMercadoPago=models.ForeignKey(ClienteMercadoPago,on_delete=models.PROTECT,blank=True)

    def __srt__(self):
        return  '{} {}'.format(self.cliente,self.tipo)

class TransferenciaActual(models.Model):
    tipo = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(User, on_delete=models.PROTECT)
    SendValue = models.CharField(max_length=50)
    accountNumber = models.IntegerField()



"""class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    correo=models.EmailField(User,max_length=100)

    def __srt__(self):
        return '{}'.format(self.correo)"""
