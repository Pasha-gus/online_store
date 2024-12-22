from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **options):
        category_1 = Category.objects.get(name="Телефоны")
        category_2 = Category.objects.get(name="Телевизоры")
        category_3 = Category.objects.get(name="Наушники")
        products = [
            {"name": "Телефон1", "description": "Описание телефона1", "category": category_1, "purchase_price": 150000},
            {"name": "Телефон2", "description": "Описание телефона2", "category": category_1, "purchase_price": 50000},
            {"name": "Телефон3", "description": "Описание телефона3", "category": category_1, "purchase_price": 20000},
            {"name": "Телевизор1", "description": "Описание телевизора1", "category": category_2, "purchase_price": 100000},
            {"name": "Телевизор2", "description": "Описание телевизора2", "category": category_2, "purchase_price": 150000},
            {"name": "Наушники1", "description": "Описание наушников1", "category": category_3, "purchase_price": 10000},
            {"name": "Наушники2", "description": "Описание наушников2", "category": category_3, "purchase_price": 5000},
        ]
        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))

