from django.shortcuts import render
from .models import Product

def store (request):
    products = Product.objects.all ()

    context = {
        "products": products,
        "total_products": products.count (),
    }
    return render (request, "store/index.html", context)