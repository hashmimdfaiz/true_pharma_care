from django.contrib import admin
from django.urls import path
from .views import addUser

urlpatterns = [
    path('add', addUser, name = 'homepage')
]
