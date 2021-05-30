from django.shortcuts import render, redirect
from .forms import ext_UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User


def new_user(request):
    form = ext_UserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'User created succesfully')
            return redirect("login")
    context = {
        "form": form
    }

    return render(request, "users/new_user.html", context)


def user_page(request):

    username = request.user.username
    email = request.user.email
    password = request.user.password

    context = {
        "username": username,
        "email": email,
        "password": password
    }

    return render(request, 'users/user_page.html', context)


def change_password(request):

    if request.method == "POST":
        u = User.objects.get(username=request.user.username)
        new_password = request.POST["password"]
        u.set_password(new_password)
        u.save()
        messages.success(request, 'Password updated')

        return redirect("login")


def change_email(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        new_email = request.POST["email"]
        user.email = new_email
        user.save()

        return redirect("user_page")


def delete_user(request):
    user = User.objects.get(username=request.user.username)
    user.delete()
    return redirect("new_user")
