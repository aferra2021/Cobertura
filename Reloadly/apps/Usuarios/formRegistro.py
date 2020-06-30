from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import Cliente
from django import forms

#UserCreationForm
class RegistroFormUsuario(UserCreationForm):

    class Meta:
        model = User
        fields=[
            'username',
            'email',
            'password1',
            'password2',
        ]

        labels={
            'username':'Nombre de Usuario',
            'email':'Correo',
            'password1':'Contraseña',
            'password2':'Confirmar Contraseña',
        }

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        """widgets={
		'rga':forms.Select(attrs={'class':'form-control','id':'rga'}),
		'plaza':forms.Select(attrs={'class':'form-control','id':'plaza'}),
		'firmaEntidad':forms.TextInput(attrs={'class':'form-control','id':'firmaEntidad'}),
		'firmaContratado':forms.TextInput(attrs={'class':'form-control','id':'firmaContratado'}),
		'fechaInicio':forms.TextInput(attrs={'class':'form-control ','id':'fechaInicio'}),
		'fechaFin':forms.TextInput(attrs={'class':'form-control','id':'fechaFin'}),
		}"""