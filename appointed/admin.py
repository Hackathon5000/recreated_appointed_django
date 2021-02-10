from django.contrib import admin

# Register your models here.
from django.contrib import admin 
from .models import Patient, VaccCenter

admin.site.register(VaccCenter)
admin.site.register(Patient)