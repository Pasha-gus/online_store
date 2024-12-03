from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from .models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactView(TemplateView):
    template_name = "catalog/contacts.html"


# def contacts(request):
#     return render(request, 'contacts.html')
#
#

