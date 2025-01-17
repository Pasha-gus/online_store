from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductsByCategoryView, CategoryListView
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('contacts/', ContactView.as_view(), name="contacts"),
    path('product_detail/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product_form/', ProductCreateView.as_view(), name="product_create"),
    path('catalog/<int:pk>/update', ProductUpdateView.as_view(), name="product_update"),
    path('catalog/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete"),
    path("category/", CategoryListView.as_view(), name="category_list"),
    path('category_detail/<int:pk>/', ProductsByCategoryView.as_view(), name='products_by_category')
]
