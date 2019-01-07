from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    
    #path('login/',views.login, name='login')
    path('set/',views.setsession),
    path('get/',views.getsession),
    path('setcookie/',views.setcookie),
    path('getcookie/',views.getcookie),
    ]

