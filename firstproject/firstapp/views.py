from django.shortcuts import render,HttpResponse
from .models import Login_details,Form_newdetails
from .forms import User_form

# Create your views here.
def demo(request):
	return 	render(request,'template/login.html')

	
def entry(request):
	User=request.GET['xyz']
	Password=request.GET['pass']
	 

	f=Login_details(user=User,password=Password)
	f.save()

	return HttpResponse("Saved Successfully")

def details(request):
	re= Login_details.objects.all()

	return render(request,'template/details.html', {'record':re})


def form(request):
	if request.method=='POST':
		form=User_form(request.POST)

		if form.is_valid():
			Username=form.cleaned_data['Username']
			Email=form.cleaned_data['Email']
			Contact=form.cleaned_data['Contact']
			Course=form.cleaned_data['Course']
			p=Form_newdetails(username=Username,email=Email,contact=Contact,course=Course)
			p.save()

			return HttpResponse("Saved Successfully")

	else:
		form=User_form()

	return render(request, 'template/form.html', {'form':form} )


def form_details(request):
	fo=Form_newdetails.objects.all()

	return render(request,'template/form_details.html',{'record':fo})

