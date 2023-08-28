from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('releases', views.releases),
    path('submitted', views.submitted),
    path('artists', views.artists),
    path('videos/', views.videos),
    path('videos/<str:slug>', views.videoModal, name='videomodal'),
    path('events/', views.events),
    path('corporate', views.corporate),
]
