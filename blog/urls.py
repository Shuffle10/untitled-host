from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.blogs),
    path('<str:slug>', views.blogpost, name='blogpost')

]
