from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_details.html'
    context_object_name = 'product'


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *arg, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо {name}. Сообщение получено.')


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'

# def home(request):
#     return render(request, 'catalog/home.html')
#
#
# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         return HttpResponse(f'Спасибо {name}. Сообщение получено.')
#     return render(request, 'catalog/contacts.html')
#
#
# def product_details(request, product_id):
#     product = Product.objects.get(id=product_id)
#     context = {
#         'product_image': product.image,
#         'product_name': product.name,
#         'product_category': product.category,
#         'product_price': product.price,
#         'product_description': product.description
#     }
#     return render(request, 'catalog/product_details.html', context=context)
#
#
# def product_list(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'catalog/home.html', context=context)
#
#
# def index(request):
#     return render(request, 'catalog/base.html')
