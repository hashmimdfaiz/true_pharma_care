from django.contrib import admin
from django.urls import path
from .views import addProvider, addUser

urlpatterns = [
    path('add', addUser, name = 'homepage'),
    path('addProvider', addProvider, name = 'Add Provider'),
]
