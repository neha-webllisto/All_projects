from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    
	path('register/', views.register, name = 'register'),

	path('account_activation_sent/', views.account_activation_sent, name = 'account_activation_sent'),

	path('activate/', views.activate, name = 'activate'),

]