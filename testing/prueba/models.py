from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


# Create your models here.
class usuarios(models.Model):
    
   nombre = models.CharField(max_length= 150)
   url = models.URLField(max_length= 150)
   email = models.EmailField(max_length=50)
   contraseña = models.CharField(max_length=50)
   created_At = models.DateTimeField(auto_now_add=True)
   
   class Admin:
        list_display   = ('nombre', 'url', 'email')
        list_filter    = ('nombre', 'email')
        ordering       = ('-nombre',)
        search_fields  = ('nombre',)
   
   def __str__(self):
       return self.nombre