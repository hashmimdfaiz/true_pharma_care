from django.contrib import admin
from .models import Doctor

# Register your models here.

class For_Doctor(admin.ModelAdmin):
    list_display = ['user_id','name','speciality', 'phone_number','email_id','password']

admin.site.register(Doctor,For_Doctor)