from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create-user/", views.create_user, name="create-user"),
    path("success-page/", views.success_page, name="success-page"),
    path("study/", views.study, name="study"),
    path("edit/", views.edit, name="edit"),
]
