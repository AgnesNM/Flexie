from django.urls import path

from FlexieApp import views

app_name = "FlexieApp"

urlpatterns = [
    path("", views.flexie, name = "flexie"), 
    path("about/", views.about, name = "about")

]