from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User
# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        number=request.POST["number"]
        password=request.POST["password"]
        
        User.objects.create(username=username,number=number,password=password)
        return render(request,"index.html",{"User":User})
    else:
        return render(request,"login.html")


def home(request):
    return render(request,"home.html")

def index(request):
    user = request.user
    return render(request,"index.html",{"user":user})