from audioop import reverse
from lib2to3.fixes.fix_input import context

from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProductForm
from .models import Product, Category
from .services import ProductsServices


class ProductUnpublishView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У вас нет права отменить публикацию')

        product.publication_status = True
        product.save()

        return redirect('catalog:home')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/delete_product.html'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            return HttpResponseForbidden('У вас нет прав на удаление продукта')
        if not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden('У вас нет права удалять продукт')
        return super().dispatch(request, *args, **kwargs)



class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return ProductsServices.get_list_products_from_cache()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # передаем все категории
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_details.html'
    login_url = 'users:login'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    login_url = 'users:login'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    login_url = 'users:login'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            return HttpResponseForbidden('У вас нет прав на редактирование продукта')
        if not request.user.has_perm('catalog.change_product'):
            return HttpResponseForbidden('У вас нет прав на редактирование продукта')
        return super().dispatch(request, *args, **kwargs)


class ContactsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/contacts.html'
    login_url = 'users:login'

    def post(self, request, *arg, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо {name}. Сообщение получено.')


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


class ProductsByCategoryView(View):

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        products = ProductsServices.get_products_by_category(category_id)
        context = {
            'category': category,
            'products': products
        }
        return render(request, 'catalog/products_list.html', context)