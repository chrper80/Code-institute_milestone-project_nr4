from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categories/<category_id>', views.categories, name="categories"),
]
