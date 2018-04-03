from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Image, Comment


def login(request):
    return render(request,'login.html')

def index(request):
    user = request.user
    if user.is_authenticated:
        all_images = Image.objects.all().order_by('-created_at')
        return render(request, 'feed.html', context={
            'images' : all_images
        })
    else:
        return render(request, 'login.html') 

def feed(request):
    user = request.user
    if user.is_authenticated:
        all_images = Image.objects.all().order_by('-created_at')
       
        return render(request, 'feed.html', context={
            'images' : all_images ,
            
        })
    else:
        return render(request, 'login.html') 

def explore(request):
    return HttpResponse("explore page")

def profile(request):
    user = request.user
    if user.is_authenticated:
        all_images = Image.objects.all().order_by('-created_at')
        return render(request, 'profile.html', context={
            'images' : all_images
        })
    else:
        return render(request, 'login.html') 





