from django.shortcuts import render, redirect
from .forms import ext_UserCreationForm, ChangingStuff, ChangePassword
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
    initial_data = {
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "username": request.user.username,
        "email": request.user.email,
    }
    form = ChangingStuff(initial=initial_data)
    change_password_form = ChangePassword()
    username = request.user.username

    context = {
        "form": form,
        "change_password_form": change_password_form,
        "username": username
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
        form = ChangingStuff(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]
            user.save()

        return redirect("user_page")


def delete_user(request):
    user = User.objects.get(username=request.user.username)
    user.delete()
    return redirect("new_user")
