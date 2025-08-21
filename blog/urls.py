from django.urls import path
from catalog.apps import CatalogConfig
from . import views
from .views import BlogDetailView, BlogListViews, BlogCreateView, BlogUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('<int:pk>/', BlogDetailView.as_view(), name='content_details'),
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='update_content'),
    path('new/', BlogCreateView.as_view(), name='create_content'),
    path('', BlogListViews.as_view(), name='content_list'),
]