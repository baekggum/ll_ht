from django.shortcuts import render

# Create your views here.

def new_base(request):
    return render(request, 'new_base.html')    