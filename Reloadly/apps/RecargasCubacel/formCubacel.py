from django import forms
from apps.RecargasCubacel.models import TranferenciaCubacel

class TranferenciaCubacelForm(forms.ModelForm):

    class Meta:
        model=TranferenciaCubacel
        labels={
            #esto es un diccionario a la derecha la clave y a la izquierda lo q se mostrara en la pagina
        }
        fiels=[
            #aki va el atributo de la base de datos con quien tene q emparejarse
        ]
        
        id = models.BigIntegerField(primary_key=True)
        tipo = models.CharField(max_length=50)
        fecha = models.DateTimeField()
        cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
        SendValue = models.IntegerField()
        accountNumber = models.IntegerField()
