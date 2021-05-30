from django.shortcuts import render
from .models import Category


def index(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }
    return render(request, 'store/index.html', context)
