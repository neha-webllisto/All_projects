from django.shortcuts import render

# Create your views here.
def base(request):
	return render(request,'base.html')

def form(request):
	return render(request,'form.html')

def home(request):
	return render (request,'homepage.html')

def login(request):
	return render (request,'loginpage.html')

def contact(request):
	return render (request,'contact.html')

def product(request):
	return render (request,'product.html')

def services(request):
	return render (request,'services.html')