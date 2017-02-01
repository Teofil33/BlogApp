from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout,
	)

from django.shortcuts import render, redirect

from .forms import UserLoginForm

def login_view(request):
	title = "Login"
	form  = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect("posts:list")

	context = {
		"form": form,
		"title": title,
	}	

	return render(request, "login.html", context)

def register_view(request):
	return render(request, "register.html", {})		 


def logout_view(request):
	logout(request)
	return render(request, "logout.html", {})
