from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ContactsTemplateView, HomeTemplateView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductsByCategoryView

app_name = CatalogConfig.name

urlpatterns = [
    path('product_details/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_details'),
    path('home/', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('', HomeTemplateView.as_view(), name='hi'),
    path('home/create_product/', ProductCreateView.as_view(), name='create_product'),
    path('home/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('home/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('home/<int:category_id>/products_list/', ProductsByCategoryView.as_view(), name='products_by_category'),
]