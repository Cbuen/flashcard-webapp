from django import forms
from .models import Users, Cards


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["userfirstname", "userlastname", "useremailaddress"]
        labels = {
            "userfirstname": "First Name",
            "userlastname": "Last Name",
            "useremailaddress": "Email Address",
        }
        widgets = {
            "userfirstname": forms.TextInput(attrs={"class": "form-control"}),
            "userlastname": forms.TextInput(attrs={"class": "form-control"}),
            "useremailaddress": forms.EmailInput(attrs={"class": "form-control"}),
        }

class cardForm(forms.ModelForm):
    class Meta:
        model = Cards
        fields = ["term", "definition", "setid"]
        widgets = {
            "term": forms.TextInput(attrs={"class": "form-control"}),
            "definition": forms.TextInput(attrs={"class": "form-control"}),
            "setid": forms.NumberInput(attrs={"class": "form-control"}),
        }
