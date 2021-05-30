from django.urls import path
from . import views

urlpatterns = [
    path("new_user/", views.new_user, name="new_user"),
    path("user_page/", views.user_page, name="user_page"),
    path("change_password/", views.change_password, name="change_password"),
    path("change_email/", views.change_email, name="change_email"),
    path("delete_user/", views.delete_user, name="delete_user"),
]
