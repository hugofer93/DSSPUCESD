from django import forms
from django.core.validators import RegexValidator

from DSSPUCESD import models

class Form_Persona(forms.ModelForm):
    nombre = forms.CharField(max_length=45,
                            widget = forms.TextInput(attrs = {'placeholder':'Nombres','class':'form-control','id':'nombres'}))

    apellido = forms.CharField(max_length=45,
                            widget = forms.TextInput(attrs = {'placeholder':'Apellidos','class':'form-control','id':'apellidos'}))

    cedula = forms.CharField(max_length=10, min_length=10, validators=[RegexValidator(r'^\d{10}$')],
    						widget = forms.NumberInput(attrs={'placeholder': 'Numero de Cedula','class':'form-control','id':'cedula'}))
    
    direccion = forms.CharField(max_length=80,
    						widget = forms.Textarea(attrs = {'placeholder': 'Direccion','class':'form-control','id':'direccion','rows':'2'}))
    
    telefono = forms.CharField(max_length=45, validators=[RegexValidator(r'^[0-9 ]+$')],
    						widget = forms.TextInput(attrs = {'placeholder': 'Numero Telefono','class':'form-control','id':'telefono'}))
    
    email = forms.EmailField(max_length=30,
    						widget = forms.EmailInput(attrs = {'placeholder': 'email@ejemplo.com','class':'form-control','id':'email'}))
    
    estado = forms.BooleanField(required=False,initial=True)
    
    class Meta:
        model = models.Persona
        fields = ['nombre','apellido','cedula','direccion','telefono','email','estado']

