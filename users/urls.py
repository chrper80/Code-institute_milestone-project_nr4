from django.urls import path
from . import views

urlpatterns = [
    path("new_user", views.new_user, name="new_user"),
    path("user_page", views.user_page, name="user_page"),
    path("delete_user", views.delete_user, name="delete_user"),
    path("change_stuff", views.change_stuff, name="change_stuff"),
    path("confirmation", views.confirmation, name="confirmation"),
]
