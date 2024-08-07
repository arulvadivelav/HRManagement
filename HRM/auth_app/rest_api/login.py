from django.shortcuts import render, redirect
from auth_app.forms import CustomLoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.views import View


def basic(request):
    return render(request, "home.html")


def login_page(request):
    return render(request, "login.html")


def registration_page(request):
    return render(request, "templates/registration.html")


class Login(View):
    def post(self, request):
        try:
            form1 = CustomLoginForm(request.POST)
            if form1.is_valid():
                username = form1.cleaned_data["username"]
                password = form1.cleaned_data["password"]
                try:
                    user_ref = User.objects.get(username=username)
                except:
                    messages.error(request, "User not found.")
                    return render(request, "login.html")
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    messages.success(request, "Logged in successfully")
                    return redirect("home")
                else:
                    messages.error(request, "Wrong password.")
                    return redirect("login_page")

        except Exception as e:
            print(e)
            messages.error(request, str(e))
            return redirect("login_page")


class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out successfully")
        return render(request, "templates/login.html")


def registration(request):
    try:
        if request.method == "POST":
            registration_form = UserRegistrationForm(request.POST)
            if registration_form.is_valid():
                username = registration_form.cleaned_data["username"]
                first_name = registration_form.cleaned_data["firstname"]
                lastname = registration_form.cleaned_data["lastname"]
                email = registration_form.cleaned_data["email"]
                password = registration_form.cleaned_data["password"]
                confirmpassword = registration_form.cleaned_data["confirmpassword"]

                if password != confirmpassword:
                    messages.error(request, "Password and confirm password must match.")
                    return render(request, "templates/registration.html")

                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username already exist.")
                    return render(request, "templates/registration.html")

                User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=lastname,
                    email=email,
                    is_staff=True,
                    password=make_password(password),
                )
                messages.success(request, "User details registerd successfully.")
                return redirect("login_page")
            else:
                messages.error(request, "Invalid input details.")
                return render(request, "templates/registration.html")
        else:
            messages.error(request, "API allows only POST method.")
            return render(request, "templates/registration.html")

    except Exception as e:
        print(e)
        messages.error(request, "Internal server error.")
        return render(request, "templates/registration.html")
