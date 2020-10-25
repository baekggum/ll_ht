from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from .models import User,Blog
import datetime
# Create your views here.

def home(request):
    blog = Blog.objects.all()
    return render(request, 'home.html', {'blog':blog})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "detail.html", {'blog':blog})

def new(request):
    return render(request, "new.html")
    
def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.pub_date = datetime.datetime.now()
    blog.content = request.POST['content']
    blog.receipt = request.FILES['receipt']
    blog.save()
    return redirect('/')

def updateAction(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.POST['title']
    blog.pub_date = datetime.datetime.now()
    blog.content = request.POST['content']
    blog.receipt = request.FILES['receipt']
    blog.save()
    return redirect('/detail/' + str(blog_id))

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "update.html", {'blog':blog})

def delete(request, blog_id):
    get_object_or_404(Blog, pk=blog_id).delete()
    return redirect('/')  

def index(request):
    user = request.user
    return render(request,"index.html",{"user":user})

def check1(request):
    return render(request,"check1.html")  

def check2(request):
    return render(request,"check2.html")
    
def company(request):
    return render(request,"cp_detail.html")

def feedback(request):
    return render(request,"feedback.html")

def qr(request):
    return render(request,"qr.html")

def main(request):
    return render(request,"main.html")

def accept_list(request):
    blog = Blog.objects.all()
    return render(request,"accept-list.html",{"blog":blog})

def qr_add(request):
    blog = Blog()
    user = User()
    user.name = request.POST['userid']
    user.phone_number = request.POST['phonenumber']
    user.password=0
    user.save()
    return redirect('/')