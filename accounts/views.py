from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
	context = {}

	if request.method == "POST":
		user = auth.authenticate(username=request.POST["email"], password=request.POST["password"])
		if user is not None:
			auth.login(request, user)
			return redirect("home")
		else:
			context["error"] = "Email or Password incorrect."

	return render(request, "accounts/login.html", context)


def signup(request):
	context = {}

	if request.method == "POST":
		# Check if the password and the confrom are the same
		if request.POST["password1"] == request.POST["password2"]:
			# Check if email is alrady been used
			try:
				user = User.objects.get(email=request.POST["email"])
				context["error"] = "This email is already registred."
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST["email"], email=request.POST["email"], password=request.POST["password1"])
				auth.login(request, user)
				return redirect("home")
		else:
			context["error"] = "Passwords must match."
	
	return render(request, "accounts/signup.html", context)


def logout(request):
	auth.logout(request)
	return redirect("login")
