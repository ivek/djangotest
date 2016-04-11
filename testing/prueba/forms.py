from django import forms

class RegForm(forms.Form):
     nombre_form = forms.CharField(max_length=100)
     email = forms.EmailField()
     contrasena = forms.CharField(max_length=100)
     