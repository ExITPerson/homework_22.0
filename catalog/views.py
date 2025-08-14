from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо {name}. Сообщение получено.')
    return render(request, 'catalog/contacts.html')


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product_image': product.image,
        'product_name': product.name,
        'product_category': product.category,
        'product_price': product.price,
        'product_description': product.description
    }
    return render(request, 'catalog/product_details.html', context=context)


def index(request):
    return render(request, 'catalog/base.html')