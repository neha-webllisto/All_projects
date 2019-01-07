from django.shortcuts import render
from .forms import Session_form
from django.http import HttpResponse
# Create your views here.

# def login(request):

# 	form = Session_form()

# 	if request.method == 'POST':
# 		form = Session_form(request.POST)

# 		if form.is_valid():
# 			username = form.cleaned_data['username']
# 			request.session['username'] = username

# 			password = form.cleaned_data['password']
# 			request.session['password'] = password
			
# 	return render(request,'login.html',{'username':username})


def setsession(request):
	request.session['username'] = 'Neha'
	request.session['password'] = 'neha1234'
	return HttpResponse("Session set ")

def getsession(request):
	username = request.session['username']
	password = request.session['password']
	return HttpResponse(username+" "+password)

def setcookie(request):
	response = HttpResponse("Cookie set")
	response.set_cookie('neha',"www.google.com")
	return response

def getcookie(request):
	cook = request.COOKIES['neha']
	return HttpResponse('neha @ : '+cook)
