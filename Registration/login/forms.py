from django.forms import ModelForm
from .models import Registers
from django import forms

class Register_form(ModelForm):
	class Meta:
		model = Registers
		fields = '__all__'

class Login_form(forms.Form):
	email = forms.EmailField()