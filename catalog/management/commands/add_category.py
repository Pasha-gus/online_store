from django.core.management.base import BaseCommand
from catalog.models import Category

class Command(BaseCommand):
    help = 'Add test categoryes to the database'

    def handle(self, *args, **options):
        categories = [
            {'name': 'Телефоны', 'description': 'Описание категории телефоны'},
            {'name': 'Телевизоры', 'description': 'Описание категории телевизоры'},
            {'name': 'Наушники', 'description': 'Описание категории наушники'}
        ]
        for category_data in categories:
            category, created = Category.objects.get_or_create(**category_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added category: {category.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Category already exists: {category.name}'))
