from django.urls import path

from . import views


urlpatterns = [
    #Admin
    
    
    #ClientSide
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('healthform', views.healthform, name='healthform'),
]