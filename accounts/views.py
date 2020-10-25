from django.shortcuts import render

# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        number=request.POST["number"]
        password=request.POST["password"]
        
        User.objects.create(username=username,number=number,password=password)
        user=User.objects.all
        for i in user:
            if(username==i.name):
                return render(request,"index.html",{"user":user})
    else:
        return render(request,"login.html")

def user_login(request):
    return render(request, "user_login.html")

def ad_login(request):
    return render(request, "admin_login.html")