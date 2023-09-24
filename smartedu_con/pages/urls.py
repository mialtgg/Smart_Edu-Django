from .import views
from django.contrib import admin
from django.urls import path
 
#path(route,view, opt(kısayol ismi))
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    
]