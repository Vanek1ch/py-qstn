from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from .models import Person

# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_protect
def index(request):
    return render(request, "index.html")

@csrf_protect
def registration(request):
    return render(request, "registration.html")

@csrf_protect
def add_user(request):
    if request.method == "POST":
        person = Person()
        person.login =  request.POST.get("login")
        person.password = request.POST.get("password")
        person.email = request.POST.get("email")
        person.number = request.POST.get("number")
        person.EI = request.POST.get("EI")
        person.date = request.POST.get("date")
        person.save()
    return HttpResponseRedirect("/")

@csrf_protect
def private_office(request):
    return render(request, "private_office.html")