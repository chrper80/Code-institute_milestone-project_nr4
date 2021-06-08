from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categories/<category_id>', views.categories, name="categories"),
    path('ind_products/<product_id>', views.ind_products, name="ind_products"),
    path('add_cart', views.add_cart, name="add_cart"),
    path("remove_from_cart/", views.remove_from_cart, name="remove_from_cart"),
    path("contact/", views.contact, name="contact"),
    path("store/", views.store, name="store"),
]
