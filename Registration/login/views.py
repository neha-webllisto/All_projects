from django.shortcuts import render
from .models import Registers
from .forms import Register_form,Login_form
from django.http import HttpResponseRedirect 

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = Register_form(request.POST)

		if form.is_valid():
			form.save()

			display = Registers.objects.all()
			return render(request, 'display.html', {'display':display})

	else:
		form = Register_form()
	return render(request, 'register.html', {'form':form})

def login(request):

	if request.method == 'POST':

		form = Register_form(request.POST)

		if form.is_valid():

			data = Registers.objects.raw('SELECT Id,Email from login_Registers')
			email = form.cleaned_data['email']

			if data.email == email:
				return HttpResponse('we match one email address')


	form = Login_form()
	return render(request,'login.html', {'form': form})