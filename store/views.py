from django.shortcuts import render
from .models import Category, Product


def index(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }
    return render(request, 'store/index.html', context)


def categories(request, category_id):

    category = Category.objects.get(id=category_id)

    all_products = Product.objects.all()

    products = []

    for i in all_products:
        if i.category.id == int(category_id):
            products.append(i)

    context = {
        "category": category,
        "products": products
    }
    return render(request, 'store/categories.html', context)


def ind_products(request, product_id):
    product = Product.objects.get(id=product_id)

    context = {
        "product": product
    }
    return render(request, 'store/individual_products.html', context)
