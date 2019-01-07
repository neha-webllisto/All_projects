from django.shortcuts import render
from .models import Data
from .forms import MyForm
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory

# Create your views here.
def demo(request):
	if request.method == 'POST':
		form = MyForm(request.POST)

		if form.is_valid():
			form.save()

			details = Data.objects.all()
			return render(request,'display.html',{'details':details})
			#return HttpResponse("Saved Successfully")

	else:
		form = MyForm()
	return render(request,'details.html',{'form':form})


def display(request):
	details = Data.objects.all()
	return render(request,'display.html',{'details':details})

# def edit(request,id):
# 	edit = Data.objects.get(id=id)
# 	form = MyForm(instance=edit)

# 	if form.is_valid():

# 		form.save()
# 		return HttpResponseRedirect('/display/')
# 	return render(request,'edit.html',{'form':form,'id':id})

def delete(request,id):
	dele = Data.objects.get(id=id).delete()
	return HttpResponseRedirect('/display/')


def edit(request,id):
	edit = Data.objects.get(id=id)
	form = MyForm(instance=edit)

	if request.method == 'POST':

		form = MyForm(request.POST, instance=edit)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/display/')

	return render(request,'edit.html',{'form':form, 'id':id})