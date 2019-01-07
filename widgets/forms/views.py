from django.shortcuts import render
from .forms import Widget_form

# Create your views here.
def form(request):
	form = Widget_form()
	return render(request,'boot.html',{'form':form})