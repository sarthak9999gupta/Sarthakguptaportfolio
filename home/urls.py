from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("",views.home, name='home'),
    #path("about",views.about, name='about'),
   #path("skills",views.skills, name='skills'),
    #path("education",views.education, name='education'),
    #path("work",views.work, name='work'),
    #path("experience",views.experience, name='experience'),
    #path("contact",views.contact, name='contact')
]