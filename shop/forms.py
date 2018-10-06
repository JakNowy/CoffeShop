from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class UserRegistrerForm(UserCreationForm):
    # confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        # widgets = {
        #     'password': forms.PasswordInput(),
        # }
        help_texts = {
            'username': None,
            'password1': None,
        }

class OrderForm(forms.Form):
    choices = (
        ('S', ("Small")),
        ('M', ("Medium")),
        ('L', ("Large")),
    )
    city = forms.CharField(max_length=30)
    street = forms.CharField(max_length=30)
    house_number = forms.CharField(max_length=10)
    size = forms.ChoiceField(choices=choices)