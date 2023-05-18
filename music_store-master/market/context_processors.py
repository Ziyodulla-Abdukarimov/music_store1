from models.models import Category
from django.shortcuts import get_object_or_404
from canfigure import title
from cart.models import CartItem
from cart.cart import CartSession
from models.models import Product


def base_context(request):
    if not request.user.is_authenticated:
        cartSession = CartSession()
        cart = cartSession.getCartItems(request)
        cart_items = []
        for product_id, product_data in cart.items():
            product = get_object_or_404(Product, id=product_id)
            cart_items.append({
                'product': product,
                'qty': product_data['qty'],
            })
        cart_count = len(request.session.get('cart', {}))
    else:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        cart_count = cart_items.count()
    return {
        'cart_count': cart_count,
        'cart_products': cart_items,
        'categories': Category.objects.filter(parent=None),
        'store_title': title
    }
