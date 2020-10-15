from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
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