from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categories/<category_id>', views.categories, name="categories"),
    path('ind_products/<product_id>', views.ind_products, name="ind_products"),
]
