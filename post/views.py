from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from post.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm, ProductEdit
from post.models import Category, Product


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def products_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            search_query = request.GET.get('search', '')
            # Исключаем объекты с пустым полем image
            products = Product.objects.exclude(image__isnull=True).filter(
                Q(name__icontains=search_query) | Q(characteristic__icontains=search_query)
            )

            paginator = Paginator(products, 3)  # 3 продукта
            page = request.GET.get('page')

            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)

            context = {"products": products, "search_query": search_query}
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


def product_edit(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    if request.method == 'GET':
        context = {
            "form": ProductEdit(instance=product)
        }
        return render(request, 'products/product_update.html', context)

    if request.method == 'POST':
        form = ProductEdit(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():
            # Проверяем, предоставлено ли новое изображение
            if 'image' in request.FILES:
                form.save()
                return redirect(f'/products/')
            else:
                # Если изображение не предоставлено, сохраняем форму без изображения
                form.save(commit=False)
                form.instance.image = product.image  # Сохраняем старое изображение
                form.save()
                return redirect(f'/products/')

        return render(
            request,
            'products/product_update.html',
            {"form": form}
        )
