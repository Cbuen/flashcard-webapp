from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create-user/", views.create_user, name="create-user"),
    path("success-page/", views.success_page, name="success-page"),
    path("study/", views.study, name="study"),
    path("edit/", views.edit, name="edit"),
    path("edit/card-set", views.edit_card_set, name="card-set"),
    path("remove-card/", views.remove_last_card, name="remove-card"),
    path("create-set/", views.create_set, name="create-set"),
    path("save-card/", views.save_card, name="save-card"),
    path("sign-in/", views.sign_in, name="sign-in"),
    path("register/", views.register, name="register"),
    path("register-load/", views.register_load, name="register-load"),
]
