from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from post.models import Category, Product

def hello_view(request):
    if request.method == 'GET':
        return render(request, 'hello_page.html')


def current_date_view(request):
    current_data = timezone.localtime()
    if request.method == 'GET':
        return render(request, 'current_date_page.html', {'current_date': current_data})


def goodbye_view(request):
    if request.method == 'GET':
        return render(request, 'goodbye_page.html')


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {"products": products}
        return render(request, 'products/products_page.html', context)


def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'products/category_list.html', {'categories': categories})


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    context = {"category": category, "products": products}
    return render(request, 'products/products_page.html', context)