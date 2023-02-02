from .models import Order
from django import forms


class OrderCreateForm(forms.ModelForm):
    full_name = forms.CharField(
        label="nom complet", widget=forms.TextInput({"class": "form-control",
                                                     "placeholder":
                                                     "nom complet"}))
    email = forms.EmailField(
        label="votre email", widget=forms.EmailInput({"class ": "form-control",
                                                      "placeholder": "email"}))

    phone = forms.CharField(
        label="telephone", widget=forms.TextInput({"class": "form-control",
                                                   "placeholder":
                                                   "telephone"}))
    addresse = forms.CharField(
        label="addresse", widget=forms.TextInput({"class ": "form-control",
                                                  "placeholder": "addresse"}))

    class Meta:
        model = Order
        fields = ("full_name", "email", "phone", "addresse")
