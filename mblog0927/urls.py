"""
URL configuration for mblog0927 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from mysite import views as mv
=======
from mysite import views as mv #從mysite 載入
>>>>>>> 278678e3942d5ed2f6a55198df342e33b8d26518
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mv.homepage,name='homepage'), #連到view的homepage
    path('post/<slug:slug>/',mv.showpost,name="showpost")
]
