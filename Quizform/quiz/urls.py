"""Quizform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views
from .views import(QuesListAPIView,)


urlpatterns = [
    path('quiz',QuesListAPIView.as_view()),
    path('addQuestion/', views.addQuestion,name='addQuestion'),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutPage,name='logout'),
    path('register/', views.registerPage,name='register'),
    path('',views.home,name='home'),
]
