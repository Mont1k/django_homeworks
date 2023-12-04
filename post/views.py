from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from post.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm
from post.models import Category, Product


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def products_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            products = Product.objects.all()
            context = {"products": products}
            return render(request, 'products/products_page.html', context)
        else:
            return redirect('/users/login/')


def category_list(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            categories = Category.objects.all()
            return render(request, 'products/category_list.html', {'categories': categories})
        else:
            return redirect('/users/login/')


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    context = {"category": category, "products": products}
    return render(request, 'products/products_page.html', context)


def products_detail_view(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/products_detail.html', context)


@login_required
def product_create(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create_product.html', context)
    if request.method == "POST":
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)

            return redirect('/products')

        context = {
            'form': form
        }

    return render(request, 'products/create_category.html', context)


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()  # сохраняет
            return redirect('/categories')

    else:
        form = CategoryCreateForm()

    context = {'form': form}
    return render(request, 'products/create_category.html', context)


@login_required
def review_create(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('/products')

    else:
        form = ReviewCreateForm()

    context = {'form': form, 'product': product}
    return render(request, 'products/create_review.html', context)
