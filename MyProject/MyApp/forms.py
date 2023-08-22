from django import forms
from django.forms import ModelForm


class Signuplist(forms.Form):
    name = forms.CharField(label="nom", max_length=200)
    lastname = forms.CharField(label="Prenom", max_length=200)
    email = forms.EmailField(label="Email", max_length=250, required=False)
    phone = forms.CharField(label="Phone Number", max_length=12)

class loginlist(forms.Form):
    username = forms.CharField(label="username", max_length=50)
    password = forms.CharField(label="password", max_length=50)

