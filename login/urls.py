from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Registration/',views.registration,name='registration'),
    path('Forgetpassword/',views.forgetpassword,name='forgetpassword'),
    path('login/',views.login,name='login'),
    path('result/',views.result,name='result'),
    
]
