from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import (
    UserForm,
    cardForm,
    createSetForm,
    UserCreationForm,
)
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


def home(request):
    return render(request, "index.html")


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success-page")  # Make sure you have this URL name defined
    else:
        form = UserForm()
    return render(request, "create_user.html", {"form": form})


def success_page(request):
    return render(request, "success.html")


@login_required(login_url="/login")
def study(request):
    user_setid = 1
    user_selected_set = "Select A Set"
    card_sets = Sets.objects.filter(userid=request.user.id)
    card_set = Cards.objects.filter(setid=user_setid)

    if request.method == "POST":
        user_selected_set = request.POST.get("selected_card")
        user_selected_set = user_selected_set.split("|")

    if (
        isinstance(user_selected_set, str)
        and user_selected_set.lower() == "select a set"
    ):
        return render(
            request,
            "study.html",
            {
                "card_set": card_set,
                "card_set_list": card_sets,
                "user_selected_set_name": user_selected_set,
            },
        )
    card_set = Cards.objects.filter(setid=user_selected_set[1])
    return render(
        request,
        "study.html",
        {
            "card_set": card_set,
            "card_set_list": card_sets,
            "user_selected_set_name": user_selected_set[0],
            "user_selected_set_id": user_selected_set[1],
        },
    )


@login_required(login_url="/login")
def edit(request):
    card_sets = Sets.objects.filter(userid=request.user.id)

    # checks if user has any sets
    if Sets.objects.filter(userid=request.user.id).first() != None:
        if Sets.objects.filter(userid=request.user.id).first().setid:
            user_selected_set = (
                Sets.objects.filter(userid=request.user.id).first().setid
            )
    else:
        user_selected_set = 1

    if request.method == "POST":
        user_selected_set = request.POST.get("selected_set")
        user_selected_set = user_selected_set.split("|")
        selected_set_id = user_selected_set[1]

        card_set = Cards.objects.filter(setid=selected_set_id)
        print(selected_set_id)
        return render(
            request,
            "edit.html",
            {
                "card_sets": card_sets,
                "card_set": card_set,
                "card_setid": int(selected_set_id),
            },
        )

    card_set = Cards.objects.filter(setid=user_selected_set)

    return render(
        request,
        "edit.html",
        {"card_sets": card_sets, "card_set": card_set, "card_setid": user_selected_set},
    )


def set_editor(request):
    return render(request, "set_editor.html")

# checks if term and def are not empty
def edit_card_set(request):
    if request.method == "POST":
        form = cardForm(request.POST)
        if form.is_valid() and request.POST.get("term") and request.POST.get("definition"):
            form.save()
            return redirect("edit")  # Make sure you have this URL name defined
    else:
        form = cardForm()

    return redirect("edit")


# if user slected card to delete, delete that card
# if user did not select a card to delete, delete the last card
def remove_card(request):
    card_id = request.POST.get("card_delete_id")
    if card_id:
        Cards.objects.filter(cardid=card_id).delete()
    else:
        last_card = Cards.objects.last()
        last_card.delete()

    return redirect("edit")


def remove_last_card(request):
    card_setid = request.POST.get("card_setid")

    print(card_setid)

    last_card = Cards.objects.filter(setid=card_setid).last()

    if last_card:
        last_card.delete()
        print("Removed card")
    else:
        print("No card found")
    return redirect("edit")


def create_set(request):

    return render(request, "create_set.html")

# add some type of confirmation before deleting set
def delete_set(request): 
    set_id = request.POST.get("delete_set_id")

    if Sets.objects.filter(setid=set_id):
        if Cards.objects.filter(setid=set_id).count() > 0:
            Cards.objects.filter(setid=set_id).all().delete()

        Sets.objects.filter(setid=set_id).delete()
    else:
        print("No cards found")
    return redirect("edit")


def save_card(request):
    if request.method == "POST":
        form = createSetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("edit")

    return redirect("create-set")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(request.user.id)
            return redirect("home")
        else:
            return render(request, "login.html")

    return render(request, "login.html")


def logout_user(request):
    logout(request)

    return redirect("home")


def register(request):
    return render(request, "register_user.html")


def register_load(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = UserCreationForm()

    return redirect("register")


@login_required(login_url="/login")
def password_change(request):
    return render(request, "password_change.html")


def password_change_done(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)

        print(request)
        if form.is_valid():
            form.save()
            return redirect("home")
    return redirect("password_change")
