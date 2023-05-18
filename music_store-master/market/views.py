from django.shortcuts import render, get_object_or_404
from models.models import Product, Category
from cart.cart import CartSession


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')


def contact(request):
    return render(request, 'contact.html')


def category_detail(request, pk):
    products = Product.objects.filter(category=pk)
    category_name = Category.objects.get(id=pk).name
    return render(request, 'product.html', {
        'category_name': category_name,
        'products': products
    })


def product_detail(request, pk, id):
    cartSession = CartSession()
    if request.method == 'POST':
        if 'addtocart' in request.POST:
            qty = int(request.POST['qty'])

            cartSession.cartAddSession(request, qty, id)

    return render(request, 'product_detail.html', {
        'product': get_object_or_404(Product, id=id),
        'recommended': Product.objects.filter(category=Category.objects.get(id=pk))
    })
