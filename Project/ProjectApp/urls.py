from django.contrib import admin
from django.urls import path,include
from Project import views

urlpatterns = [
    path('boy', views.home, name='home')
]