"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index_page'),
    path('hello/', views.hello_view),
    path('current_date/', views.current_date_view, name='current_date'),
    path('goodbye/', views.goodbye_view),
    path('products/', views.products_view),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_products, name='category_products'),
    path('product/<int:product_id>/', views.products_detail_view),
    path('create_products', views.product_create),
    path('create_categories', views.category_create),
    path('create_reviews/<int:product_id>/', views.review_create, name='create_review'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)