from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login', loginPage, name='login'),
    path('register', registerPage, name='register'),
    path('me', me, name='me'),
    path('logout', doLogout, name='logout'),
]

