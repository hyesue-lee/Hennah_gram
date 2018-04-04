from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Image, Comment, Like
from django.contrib.auth.models import User


def login(request):
    return render(request,'login.html')

def index(request):
    user = request.user
    if user.is_authenticated:
        all_images = Image.objects.all().order_by('-created_at')
        return render(request, 'feed.html', context={
            'images' : all_images ,
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
    user = request.user
    if user.is_authenticated:
        all_users = User.objects.all()
        return render(request, 'explore.html', context={
            'users' : all_users ,    
        })
    else:
        return render(request, 'login.html')

def profile(request):
    user = request.user
    if user.is_authenticated:
        all_images = Image.objects.all().order_by('-created_at')
        return render(request, 'profile.html', context={
            'images' : all_images ,
        })
    else:
        return render(request, 'login.html') 

def like(request):
    user = request.user
    if user.is_authenticated:
        all_likes = Like.objects.all().order_by('-created_at')
        all_images = Image.objects.all().order_by('-created_at')
        return render(request, 'like.html', context={
            'likes' : all_likes ,
            'images' : all_images ,
        })
    else:
        return render(request, 'login.html') 




