
from django.urls import path
from .models import Product
from products.views import product_detail_view, products_view

urlpatterns = [
    path('',products_view,name='list'),
    path('<int:product_id>/', product_detail_view, name='detail'),
]
