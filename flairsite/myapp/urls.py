from django.urls import path

from . import views


urlpatterns = [
    #LOGIN,LOGOUT,REGISTER
    path('login/', views.userlogin, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    #ClientSide
    path('', views.home, name='home'),
    path('healthform', views.healthform, name='healthform'),
]