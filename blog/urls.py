from django.urls import path
from .apps import BlogConfig
from .views import BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView

app_name = 'blog'

urlpatterns = [
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='content_details'),
    path('blogs/edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('blogs/new/', BlogCreateView.as_view(), name='create'),
    path('blogs/', BlogListView.as_view(), name='content_list'),
]