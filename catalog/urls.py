from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="products_list"),
    path('contacts/', ContactView.as_view(), name="contacts"),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail')
]
