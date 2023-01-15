from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

def store (request, slug=None):
    categories = None
    products = None

    products = Product.objects.all ()

    if slug:
        categories = get_object_or_404 (Category, slug=slug)
        products = Product.objects.filter (category=categories, is_available=True)

    context = {
        "products": products,
        "total_products": products.count (),
    }
    return render (request, "store/index.html", context)

def product_detail (request, category_slug, product_slug):
    return render (request, "store/product_detail.html")