from django import forms
from .models import Users


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
