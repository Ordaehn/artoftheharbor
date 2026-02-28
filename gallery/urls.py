from django.urls import path

from . import views

app_name = "gallery"

urlpatterns = [
    path("artwork/", views.artwork, name="artwork"),
    path("tattoo/", views.tattoo, name="tattoo"),
]
