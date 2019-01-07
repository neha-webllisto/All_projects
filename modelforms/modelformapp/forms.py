from django.forms import ModelForm
from .models import Data




class MyForm(ModelForm):
	class Meta():
		model = Data
		fields = '__all__'