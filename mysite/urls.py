"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import  path , include
from django.contrib import admin
from images import views #이미지 앱의 뷰 임폴트
from django.conf import settings
from django.conf.urls.static import static

#include함수: 다른 URLconf들을 참조.
#Django 가 함수 include() 를 만나게 되면, URL 의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include 된 URLconf 로 전달


urlpatterns = [
    path('admin/', admin.site.urls),
    path('images/', include('images.urls')),
    path('', views.index, name='index'),
    path('feed/', views.feed, name='feed'),
    path('explore/', views.explore, name='explore'),
    path('profile/', views.profile, name='profile'),
    path('like/', views.like, name='like'),
    path('login/', views.login, name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#static함수에 첫번째인자로 url,키워드 인자로 경로전달