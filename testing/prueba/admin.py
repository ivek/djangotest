from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib import admin
from prueba.models import usuarios


class adminusuarios(admin.ModelAdmin):
     list_display = [ '__str__', "nombre", "email"]
     class meta:
          model = usuarios
         
# Register your models here.
admin.site.register(usuarios, adminusuarios)