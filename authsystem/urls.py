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
    path('about/', views.s_about, name='about'),
    path('fine/', views.s_fine, name='fine'),
    path('reserve/', views.s_reserve, name='reserve'),
    path('borrowedbooks/', views.s_borrowbook, name='borrowbook'),
    path('borrowhistory/', views.s_borrowhistory, name='borrowhistory'),
    path('profile/', views.s_profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('bookstatistics/', views.bookstats, name='stats'),
    path('bookupdate/', views.bookupdate, name='update'),
    path('fineimposition/', views.fineimpo, name='fineimpo'),
    path('datamanipulation/', views.datamanip, name='datamanip'),
]