from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()

			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponse("Register Successfully")

	else:
		form = UserCreationForm()

	return render(request, 'register.html', {'form':form})





def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			subject = 'Activate your Account'
			message = render_to_string('account_activation_email.html', {'user':user, 'domain':current_site.domain, 'uid':urlsafe_base64_encode(force_bytes(user.pk)), 'token':account_activation_token.make_token(user),})
			user.email_user(subject, message)
			return redirect('account_activation_sent')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form':form})	
