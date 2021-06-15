from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ext_UserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')

    password2 = forms.CharField(
        widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

        help_texts = {
            'username': None,
        }

    def clean_email(self):
        all_user_emails = []
        all_users = User.objects.all()
        for user in all_users:
            all_user_emails.append(user.email)

        email_passed = self.cleaned_data.get("email")
        if email_passed in all_user_emails:
            raise forms.ValidationError(
                "A user with that email already exists")
        return email_passed


class ChangingStuff(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class ChangePassword(forms.ModelForm):
    class Meta:
        model = User
        fields = ["password"]
        widgets = {
            "password": forms.PasswordInput(attrs={
                "placeholder": "Enter your new password",
                "minlength": 8,
            })
        }

        error_messages = {
            "password": {
                "required": "This field is required",
                "min_length": "At least 8 characters is required",
                "max_length": "To long, only 128 characters are allowed",
            }
        }

    def clean_password(self):
        password_passed = self.cleaned_data.get("password")
        length = len(password_passed)
        if length < 8:
            raise forms.ValidationError("At least 8 characters required")
        return password_passed
