from django.urls import path

from FlexieApp import views

app_name = "FlexieApp"

urlpatterns = [
    path("", views.index_view, name = "index_view"),
    path("about/", views.about, name = "about"),
    path("results/", views.results_view, name = "results_view"),
    
]