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
    path("edit/delete-set", views.delete_set, name="delete_set"),
    path("save-card/", views.save_card, name="save-card"),
    path("login/", views.login_user, name="login"),
    path("register/", views.register, name="register"),
    path("register-load/", views.register_load, name="register-load"),
    path("logout/", views.logout_user, name="logout"),
    path("password_change/", views.password_change, name="password_change"),
    path(
        "password_change/done/", views.password_change_done, name="password_change_done"
    ),
]
