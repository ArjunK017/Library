from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/',views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('notification/', views.snotification, name='snotification'),
    path('bookrenewal/', views.bookrenewal, name='bookren'),
    path('tablebooking/', views.tablebook, name='tableb'),
]