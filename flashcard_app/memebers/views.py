from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm
from .models import *

# Create your views here.


def members(request):
    # set names list
    card_set_names = Sets.objects.values_list("setname", flat=True)
    return render(request, "index.html", {"card_set_names": card_set_names})


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success_page")  # Make sure you have this URL name defined
    else:
        form = UserForm()
    return render(request, "create_user.html", {"form": form})


def success_page(request):
    return render(request, "success.html")
