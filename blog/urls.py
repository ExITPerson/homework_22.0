from django.urls import path
from .apps import BlogConfig
from .views import BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', BlogDetailView.as_view(), name='content_details'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('new/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='content_list'),
]