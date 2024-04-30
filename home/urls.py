from django.contrib import admin
from django.urls import path,include
from home import views


app_name = 'home'


urlpatterns = [

#react app

path("",views.index,name='home'),

path("about/",views.index_about,name="tgrwa_about"),

path("services/",views.index_services,name="tgrwa_services"),

path("team/",views.index_team,name="tgrwa_team"),


path("projects/",views.index_projects,name="tgrwa_projects"),


path("postpage/",views.index_postpage,name="tgrwa_postpage"),

path("contact/",views.index_contact,name="tgrwa_contact"),

#path("contactinfo",views.contactinfo,name='contactinfo'),








]






