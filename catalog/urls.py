from django.urls import path
from catalog.apps import CatalogConfig
from . import views
from .views import ProductListView, ProductDetailView, ContactsTemplateView, HomeTemplateView, ProductCreateView, \
    ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('product_details/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('home/', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('', HomeTemplateView.as_view(), name='home'),
    path('home/create/', ProductCreateView.as_view(), name='create_product'),
    path('home/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product')
]