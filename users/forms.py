from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ext_UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


class ChangingStuff(forms.Form):
    first_name = forms.CharField(max_length=100,  widget=forms.TextInput(
        attrs={'class': 'input', "placeholder": "Enter new first name"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'input', "placeholder": "Enter new last name"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'input', "placeholder": "Enter new email"}))
