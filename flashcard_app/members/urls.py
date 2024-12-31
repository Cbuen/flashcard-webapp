from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create-user", views.create_user, name="create_user"),
    path("success_page", views.success_page, name="success_page"),
    path("study", views.study, name="study"),
    path("edit", views.edit, name="edit"),
]
