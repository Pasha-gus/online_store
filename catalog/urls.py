from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_description

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('product_description/<int:product_id>', product_description, name='product_description')
]
