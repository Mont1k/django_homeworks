from django.urls import path

from post import views

urlpatterns = [
    path('', views.index_view, name='index_page'),
    path('products/', views.products_view, name='products_view'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_products, name='category_products'),
    path('product/<int:product_id>/', views.products_detail_view, name='product_detail'),
    path('products/create_products/', views.product_create, name='product_create'),
    path('products/<int:product_id>/edit/', views.product_edit, name='product_edit'),
    path('create_categories', views.category_create),
    path('create_reviews/<int:product_id>/', views.review_create, name='create_review'),
]
