from django.db import models
from django.contrib.auth.models import User
# Create your models here.


"""class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    correo=models.EmailField(User,max_length=100)

    def __srt__(self):
        return '{}'.format(self.correo)"""

class TranferenciaCubacel (models.Model):
    tipo=models.CharField(max_length=50)
    fecha=models.DateTimeField()
    cliente=models.ForeignKey(User,on_delete=models.CASCADE)
    SendValue=models.IntegerField()
    accountNumber=models.IntegerField()

    def __srt__(self):
        return  '{} {}'.format(self.cliente,self.tipo)

class TransferenciaActual(models.Model):
    tipo = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(User, on_delete=models.PROTECT)
    SendValue = models.CharField(max_length=50)
    accountNumber = models.IntegerField()
