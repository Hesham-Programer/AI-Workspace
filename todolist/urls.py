from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home_page"),
    path("edit/<int:note_id>", views.edit, name="edit")
]