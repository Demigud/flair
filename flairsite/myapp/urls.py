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

    #Dashboard
    path('dashboard', views.dashboard, name='dashboard'),
    path('submissions', views.submissions, name='submissions'),
    path('userlogs', views.userlogs, name='userlogs'),
    path('livefeed', views.livefeed, name='livefeed'),
]