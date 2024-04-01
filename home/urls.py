from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about_page, name='about-page'),
    path('support/', views.support_page, name='support-page'),
    path('privacy_policy/', views.privacy_page, name='privacy-page'),
]