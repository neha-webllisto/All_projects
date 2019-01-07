from django.contrib import admin

# Register your models here.
from .models import Login_details,Form_newdetails
admin.site.register(Login_details)
admin.site.register(Form_newdetails)