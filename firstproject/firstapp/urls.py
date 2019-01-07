from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   path('Demo/',views.demo),
   #path('Insert/',views.insert),
   path('Entry/',views.entry,name='data_entry'),
   path('Details/',views.details),
   path('Form/',views.form, name='form_entry'),
   path('Form_Details/',views.form_details),
]