from django.db import models

# Create your models here.
class Doctor(models.Model):
    user_id = models.CharField(max_length=20,primary_key=True,null=False,blank=False)
    name = models.CharField(max_length=20)
    speciality = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)



