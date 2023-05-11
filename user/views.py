from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def register(request):
	if request.user.is_authenticated:
		return redirect('main')
	if request.method == 'POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f"Account created for {username}")
			return redirect('main')
	else:
		form=UserCreationForm()
	return render(request, 'users/register.html', {'form':form})

def login(request):
	if request.user.is_authenticated:
		return redirect('main')
	form=LoginForm(request.POST)
	user=authenticate(request, username=form.username, password=form.password)
	if user is not None:
		messages.success(request, f"Welcome back")
		login(request, user)
	else:
		messages.info(request, f"Username or password is incorrect!")
		return redirect('login')
	return render(request, 'users/login.html')


def logout(request):
	logout(request)