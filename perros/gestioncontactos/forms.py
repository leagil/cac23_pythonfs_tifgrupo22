from django import forms
class FormularioContacto(forms.Form):
    apellido=forms.CharField(max_length=30)
    nombre=forms.CharField(max_length=30)
    sexo=forms.CharField(max_length=1)
    dni=forms.IntegerField()
    direccion=forms.CharField(max_length=50)
    email=forms.EmailField()
    telefono=forms.IntegerField()
    tienemascota=forms.BooleanField()