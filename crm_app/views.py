from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def home(request):

    return render(request, "home.html", {})

def login_user(request):
    # check if login attempt or normal request
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully.")
            return redirect("home")
        else:
            messages.error(request, "Incorrect username or password.")
            return redirect("login")
        
    return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "You've been logged out successfully.")
    return redirect("home")

def register(request):
    # check if registration attempt or normal request
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login user
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have signed up and logged in successfully.")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})
    