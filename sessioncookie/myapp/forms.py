from django import forms

class Session_form(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)