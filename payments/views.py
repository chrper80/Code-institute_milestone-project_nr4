from django.shortcuts import render

import stripe
from django.http import JsonResponse
from store.models import Product
from django.views.generic import TemplateView
import os

stripe.api_key = os.getenv('API_KEY', '')


YOUR_DOMAIN = 'https://milestone-project4.herokuapp.com/'


def create_checkout_session(request):
    def test_def(unit_amount, name, images, quantity):
        line_item = {
            'price_data': {
                'currency': 'sek',
                'unit_amount': unit_amount,
                'product_data': {
                    'name': name,
                    'images': [images],
                },
            },
            'quantity': quantity,
        }

        return line_item

    products = {}
    cart_ids = request.session.get("cart_items", [])
    items = []
    if request.method == "POST":
        for product_id in cart_ids:
            product = Product.objects.get(id=int(product_id))
            if products.get(product.id):
                products[product.id]["counter"] += 1
            else:
                products[product.id] = {"product": product, "counter": 1}

        for v in products.values():
            unit_amount = v["product"].product_total
            name = v["product"].product_name
            images = v['product'].product_image
            quantity = v["counter"]

            items.append(test_def(unit_amount, name, images, quantity))

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=items,
                mode='payment',
                success_url=YOUR_DOMAIN + 'payments/success',
                cancel_url=YOUR_DOMAIN + 'payments/cancel',
            )
            return JsonResponse({'id': checkout_session.id}, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class CancelView(TemplateView):
    template_name = 'payments/cancel.html'


def success(request):
    del request.session['cart_items']
    return render(request, 'payments/success.html')
