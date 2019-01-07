from django import forms

class Widget_form(forms.Form):
	Name = forms.CharField(widget= forms.TextInput(attrs={'class': 'special','Placeholder':'Enter Name'}))
	Email= forms.EmailField(widget= forms.TextInput(attrs={'Placeholder':'Enter Email'}))