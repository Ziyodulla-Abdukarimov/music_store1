from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from cart.models import UserCart, CartItem
from orders.models import Order, OrderItem
from models.models import Product, Category
from canfigure import title
from config import settings
from cart.cart import CartSession


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')


def contact(request):
    return render(request, 'contact.html', {
        'categories': Category.objects.filter(parent=None), 'store_title': title})


def category_detail(request, pk):
    products = Product.objects.filter(category=pk)
    category_name = Category.objects.get(id=pk).name
    return render(request, 'product.html', {
        'category_name': category_name,
        'products': products, 'store_title': title})


def product_detail(request, pk, id):
    cartSession = CartSession()
    if request.method == 'POST':
        if 'addtocart' in request.POST:
            qty = int(request.POST['qty'])

            cartSession.cartAddSession(request, qty, id)

    if not request.user.is_authenticated:
        cart = cartSession.getCartItems(request)
        cart_items = []
        cart_count = len(request.session.get('cart', {}))
        for product_id, product_data in cart.items():
            product = get_object_or_404(Product, id=product_id)
            cart_items.append({
                'product': product,
                'qty': product_data['qty'],
            })
    else:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        cart_count = cart_items.count()
    return render(request, 'product_detail.html', {
        'product': get_object_or_404(Product, id=id),
        'store_title': title,
        'cart_count': cart_count,
        'cart_products': cart_items,
        'recommended': Product.objects.filter(category=Category.objects.get(id=pk))
    })
