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
    first_name = request.user.first_name
    last_name = request.user.last_name
    username = request.user.username
    email = request.user.email

    context = {
        "username": username,
        "email": email,
        "first_name": first_name,
        "last_name": last_name
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


def change_stuff(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        form = request.POST
        user.first_name = form["first_name"]
        user.last_name = form["last_name"]
        user.user_name = form["username"]
        user.email = form["email"]
        user.save()

        return redirect("user_page")


def delete_user(request):
    user = User.objects.get(username=request.user.username)
    user.delete()
    return redirect("new_user")
