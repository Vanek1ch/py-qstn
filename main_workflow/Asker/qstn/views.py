from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import UserManager
import hashlib as h
import datetime as dt

# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def login(request):
    login = request.POST.get("login")
    password = request.POST.get("password")
    user = authenticate()

    return render(request, "login.html")

def registration(request):
    return render(request, "registration.html")

def add_user(request):
    login = request.POST.get("login")
    password = request.POST.get("password")
    email = request.POST.get("email")

    password = (password.encode())
    salt = (str(dt.datetime.now()).encode())
    salt_hash = h.sha256(salt).hexdigest()
    hashed_password = h.sha256(password+salt).hexdigest()
    
    
    UserManager.create_user(login=login,password=hashed_password,email=email,salt=salt_hash)
    
    return render(request, "login.html")
        

def index(request):
    return render(request, "index.html")