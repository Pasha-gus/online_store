from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('contacts/', ContactView.as_view(), name="contacts"),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product_form/', ProductCreateView.as_view(), name="product_create"),
    path('catalog/<int:pk>/update', ProductUpdateView.as_view(), name="product_update")
]
