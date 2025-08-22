from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from .models import Blog


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/content_details.html'
    context_object_name = 'content'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count = obj.views_count + 1 if obj.views_count else 1

        obj.save(update_fields=['views_count'])

        if obj.views_count == 100:
            send_mail('Пост набрал 100 просмотров',
                      f'Пост {obj.title} набрал 100 просмотров',
                      settings.DEFAULT_FROM_EMAIL,
                      ['admin@example.com'],
                      fail_silently=False)
        return obj


class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/content_list.html'
    context_object_name = 'contents'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True)


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blogs/content_form.html'
    fields = ['title', 'content', 'preview']

    def get_success_url(self):
        return reverse('blog:content_details', kwargs={'pk': self.object.pk})


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blogs/content_form.html'
    fields = ['title', 'content', 'preview']

    def get_success_url(self):
        return reverse_lazy('blog:content_details', kwargs={'pk': self.object.pk})