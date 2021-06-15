from django.shortcuts import render, redirect
from .forms import ext_UserCreationForm, ChangingStuff, ChangePassword
from django.contrib import messages
from django.contrib.auth.models import User


def new_user(request):
    form = ext_UserCreationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():

            form.save()
            messages.success(request, 'User created successfully')
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

    changing_stuff_form = ChangingStuff(initial_data)

    username = request.user.username

    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        change_password_form = ChangePassword(request.POST)

        if change_password_form.is_valid():
            new_password = change_password_form.cleaned_data["password"]
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password updated')
            return redirect("login")
    else:
        change_password_form = ChangePassword()

    context = {
        "change_password_form": change_password_form,
        "changing_stuff_form": changing_stuff_form,
        "username": username,
    }

    return render(request, 'users/user_page.html', context)


def change_stuff(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        form = ChangingStuff(request.POST, instance=user)
        if form.is_valid():
            form.save()

            return redirect("user_page")


def confirmation(request):
    return render(request, "users/confirmation.html")


def delete_user(request):
    user = User.objects.get(username=request.user.username)
    user.delete()
    messages.success(request, 'User deleted')
    return redirect("new_user")
