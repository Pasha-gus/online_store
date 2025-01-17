from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from catalog.services import get_products_by_category, get_products_from_cache

from .models import Product, Category
from .forms import ProductForm, ProductModeratorForm


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(DetailView):
    model = Product


class ContactView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.is_staff:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = request.user
        if user == self.object.owner or user.has_perm("catalog.can_unpublish_product"):
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("У вас нет прав для удаления этого продукта.")


class CategoryListView(ListView):
    model = Category
    template_name = "category_list"

class ProductsByCategoryView(ListView):
    model = Product
    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        return get_products_by_category(category_id=category_id)
