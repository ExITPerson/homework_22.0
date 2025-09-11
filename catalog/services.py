from django.core.cache import cache
from unicodedata import category

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


class ProductsServices:

    @staticmethod
    def get_list_products_from_cache():
        if not CACHE_ENABLED:
            return Product.objects.all()
        key = 'products_list'
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products)
        return products


    @staticmethod
    def get_products_by_category(category_id):
        return Product.objects.filter(category_id=category_id).order_by('name')


