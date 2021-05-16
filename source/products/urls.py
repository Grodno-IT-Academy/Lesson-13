
from django.urls import path
from .models import Product
from products.views import product_detail_view, products_view, add_view

urlpatterns = [
    path('',products_view,name='product_list'),
    path('add/', add_view, name='add_product'),
    path('<int:product_id>/', product_detail_view, name='detail'),
]
