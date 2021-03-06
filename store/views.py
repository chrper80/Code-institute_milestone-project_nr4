from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import ContactForm
from django.core.mail import send_mail
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages


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

    prices = []
    for v in products_in_cart.values():
        prices.append(v["product"].product_price)

    grand_total = (sum(prices)/100) * 1.25
    vat = grand_total * 0.20

    context = {
        "products_in_cart": products_in_cart,
        "grand_total": grand_total,
        "vat": vat
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
            messages.success(request, 'Message sent!')

    form = ContactForm

    context = {
        "form": form
    }

    return render(request, "store/contact.html", context)


def store(request):
    products = Product.objects.all().order_by('category')
    if request.method == "POST":
        try:
            if request.POST["option"] == "forest":
                products = []
                all_products = Product.objects.all()
                for product in all_products:
                    if product.category.category_name == "Forest":
                        products.append(product)

            elif request.POST["option"] == "water":
                products = []
                all_products = Product.objects.all()
                for product in all_products:
                    if product.category.category_name == "Water":
                        products.append(product)

            elif request.POST["option"] == "small_things":
                products = []
                all_products = Product.objects.all()
                for product in all_products:
                    if product.category.category_name == "Small things":
                        products.append(product)

            else:
                products = Product.objects.all().order_by('category')

        except MultiValueDictKeyError:
            messages.info(request, "You didn't choose an option")
            pass

    context = {
        "products": products
    }

    return render(request, "store/store.html", context)
