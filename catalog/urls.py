from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact')
]