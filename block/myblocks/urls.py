from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [

	path('Base/',views.base),
	path('Form/',views.form),
	path('home/',views.home),
	path('login/',views.login),
	path('contact/',views.contact),
	path('product/',views.product),
	path('services/',views.services),
    
]
