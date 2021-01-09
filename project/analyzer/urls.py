
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('home/',views.home ),
    path('flipkart/',views.flipkart,name='flipkart'),
    path('flipkart_detials/',views.flipkart,name='flipkart_detials'),
]
