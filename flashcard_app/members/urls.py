from django.urls import path
from . import views

urlpatterns = [
    path("members/", views.members, name="members"),
    path("create-user/", views.create_user, name="create_user"),
    path("success_page/", views.success_page, name="success_page"),
    path("study", views.study, name="study"),
]
