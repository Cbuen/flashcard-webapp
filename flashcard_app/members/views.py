from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm, cardForm, createSetForm
from .models import *

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


def study(request):
    user_setid = 1
    user_selected_set = "Select A Set"
    card_sets = Sets.objects.all()
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


def edit(request):
    card_sets = Sets.objects.all()
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
                "card_setid": selected_set_id,
            },
        )

    card_set = Cards.objects.filter(setid=user_selected_set)

    return render(
        request,
        "edit.html",
        {"card_sets": card_sets, "card_set": card_set, "card_setid": user_selected_set},
    )


def edit_card_set(request):

    if request.method == "POST":
        form = cardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("edit")  # Make sure you have this URL name defined
    else:
        form = cardForm()

    return render(request, "edit", {"form": form})


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


def save_card(request):
    if request.method == "POST":
        form = createSetForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect("create-set")
