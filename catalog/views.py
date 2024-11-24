from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    products = Product.objects.all()
    for product in products:
        if len(product.description) > 100:
            product.short_description = product.description[:100] + '...'
        else:
            product.short_description = product.description
    context = {"products": products}
    return render(request, 'home.html', context)


def contacts(request):
    return render(request, 'contacts.html')


def product_description(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product}
    return render(request, 'product_description.html', context)
