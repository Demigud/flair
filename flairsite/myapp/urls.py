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
    path('admin/dashboard', views.dashboard, name='dashboard'),
    path('admin/submissions', views.submissions, name='submissions'),
    path('admin/userlogs', views.userlogs, name='userlogs'),
    path('admin/livefeed', views.livefeed, name='livefeed'),
    path('admin/sub-delete/<int:id>', views.subdelete, name='subdelete'),
    path('admin/user-delete/<int:id>', views.userdelete, name='userdelete'),
    
]