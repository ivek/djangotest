from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import RegForm
from .models import usuarios

# Create your views here.
def home(request):
   form = RegForm(request.POST)
   context={
        'form':form
   }
   if form.is_valid():
   
        form_data = form.cleaned_data
        abc = form_data.get('nombre_form')
        abc1 = form_data.get('email')
        abc2 = form_data.get('contrasena')
        obj = usuarios()
        obj.nombre = abc 
        obj.email= abc1
        obj.contraseña = abc2
        obj.save()
    
   return render(request, "index.html",context)
  