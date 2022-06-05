from django.contrib import admin
from django.urls import path
from sclweb import views

urlpatterns=[
    path('', views.home , name = 'Homepage'),
    path('home.html', views.home , name = 'Homepage'),
    path('login', views.signinuser , name = 'LoginPage'),
    path('login.html', views.signinuser , name = 'LoginPage'),
    path('data.html', views.data , name = 'datavariable'),
    path('bs', views.bs , name = 'bs'),
    path('gallery.html', views.gallery , name = 'gallery'),
    path('coursefee.html', views.coursefee , name = 'course'),
    path('contact.html', views.contact , name = 'contact'),
    path('lin', views.inside , name = 'LoggedIn'),
    path('signup', views.signup , name = 'SignUp'),
    path('signout', views.signout , name = 'SignOut'),
    ] 