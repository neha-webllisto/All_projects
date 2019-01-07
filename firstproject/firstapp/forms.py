from django import forms

class User_form(forms.Form):
	Username = forms.CharField(label='Name',max_length=20)
	Email = forms.EmailField(label='Email id')
	Contact = forms.CharField(label='Phone no.',max_length=12)
	Course = forms.CharField(label='Course',max_length=20)
