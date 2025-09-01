from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import SiteAsset   

from django.http import HttpResponse
from django.core.files.storage import default_storage
from .models import SiteAsset

def debug_storage(request):
    bull = SiteAsset.objects.filter(key="bull").first()
    bull_url = bull.image.url if bull else "No bull image"
    return HttpResponse(f"""
        <p>Storage backend: {default_storage}</p>
        <p>Bull image URL: {bull_url}</p>
    """)

def get_bull_image():
    return SiteAsset.objects.filter(key="bull").first()


def redirect_to_login(request):
    if request.user.is_authenticated:
        return redirect("home")
    return redirect("register")


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("register")

        user = User.objects.create_user(
            username=email, email=email, password=password, first_name=name
        )
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    context = {"bull": get_bull_image()}
    return render(request, "front_end/layout/register.html", context)


def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")

    context = {"bull": get_bull_image()}
    return render(request, "front_end/layout/login.html", context)


def home(request):
    return render(request, "front_end/layout/home.html")


def user_logout(request):
    logout(request)
    return redirect("login")

