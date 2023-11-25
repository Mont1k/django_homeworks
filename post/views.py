from django.shortcuts import render
from django.utils import timezone

from post.models import Product, Category


# Create your views here.
def main_page(request):
    if request.method == 'GET':
        return render(request, 'main_page.html')


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
        return render(request, 'category_list.html', {'categories': categories})
