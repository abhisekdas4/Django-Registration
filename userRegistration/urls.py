from django.contrib import admin
from django.urls import path, include
from .views import user_registration, home, user_login

urlpatterns = [
    path('', home, name='home' ),
    path('login/', user_login, name='login' ),
    path('register/', user_registration, name='register'),
]
