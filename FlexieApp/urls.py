from django.urls import path

from FlexieApp import views

app_name = "FlexieApp"

urlpatterns = [
    path("", views.form_view, name = "form_view"),
    path("about/", views.about, name = "about")

]