from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, PasswordInput


class ext_UserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)

    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        
        help_texts = {
            'username': None,
        }


class ChangingStuff(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()


class ChangePassword(ModelForm):
    class Meta:
        model = User
        fields = ["password"]
        widgets = {
            "password": PasswordInput(attrs={
                "placeholder": "Enter your new password",
            })
        }
