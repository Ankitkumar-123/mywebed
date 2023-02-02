from django.contrib import admin
from django.urls import path,include
from ankitweb import views
#home=ankitweb
#hello=myweb
urlpatterns = [
    path('home',views.index ,name='home'),
    path('',views.index ,name='home'),
    path('about',views.about ,name='about'),
    path('services',views.services ,name='services'),
    path('contact',views.Contact ,name='contact')
    
]