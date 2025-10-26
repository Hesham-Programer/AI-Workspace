from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<int:note_id>", views.edit_note, name="edit"),
]
