from django.shortcuts import render
from products.models import Product
# Create your views here.
def products_view(request):
    products = {
        'products': Product.objects.all()
    }
    return render(request, 'products.html',context=products)
def product_detail_view(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    products_context = {
        "title": product.name,
        'price': product.price,
        'description': product.description,
    }
    return render(request,'product.html',context=products_context)

from .forms import ProductForm

def add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            #print(help(request))
            #print(request.POST)
            post = request.POST
            Product.objects.create(name=post['name'], price=post['price'],description=post['description'], short=post['short'])
    else:
        form = ProductForm()

    context = {'form': form}

    return render(request, 'add_product.html', context=context)