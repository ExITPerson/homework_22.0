from django.core.management.base import BaseCommand
from django.core import serializers
from catalog.models import Category, Product
import json
import os


class Command(BaseCommand):
    help = 'Add product to the database and create fixture for categories and products'

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Овощи', description='Овощи наше все')

        products = [
            {'name': 'Огурцы', 'description': 'Green', 'image': '', 'category': category, 'price': 236},
            {'name': 'Капуста', 'description': 'White', 'image': '', 'category': category, 'price': 345},
            {'name': 'Помидоры', 'description': 'Red', 'image': '', 'category': category, 'price': 456},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Продукт успешно добавлен: {product.name}'))

        categories_qs = Category.objects.all()
        products_qs = Product.objects.all()

        categories_serialized = serializers.serialize('json', categories_qs)
        products_serialized = serializers.serialize('json', products_qs)

        fixture_data = json.loads(categories_serialized) + json.loads(products_serialized)

        fixture_file = 'fixture/catalog_fixture.json'
        if not os.path.exists(fixture_file):
            os.path.join(fixture_file)

        with open(fixture_file, 'w', encoding='utf-8') as f:
            json.dump(fixture_data, f, ensure_ascii=False, indent=4)

        self.stdout.write(self.style.SUCCESS(f'Фикстура успешно создана по пути: {fixture_file}'))
