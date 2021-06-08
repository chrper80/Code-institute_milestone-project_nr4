from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import ContactForm
from django.core.mail import send_mail


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


def add_cart(request):
    products_in_cart = {}
    cart_ids = request.session.get("cart_items", [])
    if request.method == "POST":
        item_id = request.POST["product_id"]
        cart_ids.append(item_id)

    for i in cart_ids:
        product = Product.objects.get(id=int(i))

        if products_in_cart.get(product.id):
            products_in_cart[product.id]["counter"] += 1
        else:
            products_in_cart[product.id] = {"product": product, "counter": 1}

    request.session["cart_items"] = cart_ids

    context = {
        "products_in_cart": products_in_cart,
    }

    return render(request, "store/cart.html", context)


def remove_from_cart(request):

    if request.method == "POST":
        cart_ids = request.session.get("cart_items", [])
        item_id = request.POST["id"]
        x = cart_ids.index(item_id)
        del cart_ids[x]

        request.session["cart_items"] = cart_ids

    return redirect("add_cart")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                f"Mail from {name}, {email}",
                message,
                email,
                ['chrper80@gmail.com'],
                fail_silently=False,
            )
    
    form = ContactForm

    context = {
        "form": form
    }

    return render(request, "store/contact.html", context)


def store(request):
    products = Product.objects.all()

    context = {
        "products": products
    }

    return render(request, "store/store.html", context )
