from django.db import models

# Create your models here.


class ClienteMercadoPago(models.Model):
    id=models.CharField(primary_key=True,max_length=100)
    email=models.EmailField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    #phone
    area_Code=models.IntegerField()
    number=models.IntegerField()
    #identifications
    type=models.CharField(max_length=20)
    numberIdentifications=models.IntegerField()
    #Fechas de creeacion y actualización
    date_created=models.DateTimeField()
    date_last_updated=models.DateTimeField(blank=True,null=True)

    def __srt__(self):
        return  '{} {}'.format(self.email,self.date_created)

