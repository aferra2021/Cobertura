from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render,redirect

# Create your models here.

#Descripcion=models.CharField(max_length=200)

class Contacto(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    accountNumber = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.PROTECT,blank=True,null=True)

    def __srt__(self):
        return '{} : {}'.format(self.name, self.accountNumber)

class Comentario(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    votosP=models.IntegerField(blank=True,null=True)
    votosN=models.IntegerField(blank=True,null=True)

    class Meta:
        ordering = [('created')]
        #ordering = ('created',asc(nulls_last=True))

class TranferenciaGeneral(models.Model):
    tipo=models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=200,blank=True,null=True)
    fecha=models.DateTimeField()
    cliente=models.ForeignKey(User,on_delete=models.CASCADE)
    SendValue=models.IntegerField()
    contacto=models.ForeignKey(Contacto,on_delete=models.PROTECT,blank=True,null=True)
    TransferRef = models.CharField(max_length=100,blank=True,null=True)

    #clienteMercadoPago=models.ForeignKey(ClienteMercadoPago,on_delete=models.PROTECT,blank=True)

    def __srt__(self):
        return  '{} {}'.format(self.cliente,self.tipo)

class TransferenciaActual(models.Model):
    tipo = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=200,blank=True,null=True)
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(User, on_delete=models.PROTECT,blank=True,null=True)
    SendValue = models.CharField(max_length=50)
    accountNumber = models.CharField(max_length=100)
    cant=models.IntegerField()
    contacto=models.ForeignKey(Contacto, on_delete=models.PROTECT,blank=True,null=True)
    def __str__(self):
        return '{} {} {} {}'.format(self.tipo,self.SendValue,self.accountNumber,self.fecha)

class ReservasHechas(models.Model):
    fechaStart=models.DateField()#fecha de inicio
    fechaEnd=models.DateField()#fecha de Fin
    cant=models.IntegerField()
    Descripcion=models.CharField(max_length=100)#title de la promocion
    id=models.CharField(primary_key=range,max_length=100)


from apps.RecargasCubacel.serviciosCubacel import recargaCubacel
@receiver(post_save, sender=ReservasHechas)
def post_save_user(sender, instance, **kwargs):
    recargaCubacel(TransferenciaActual.objects.filter(tipo="Reserva Saldo+Bono"))