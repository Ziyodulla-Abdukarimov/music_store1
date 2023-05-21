from django.shortcuts import render, get_object_or_404
from cart.cart import CartItem, UserCart
from django.db.models import Sum, F
from models.models import Product
from cart.cart import CartSession


def getPrice(product_id):
    return Product.objects.get(id=product_id).price


# Create your views here.
def cartList(request):
    cartSession = CartSession()
    if not request.user.is_authenticated:
        cart = cartSession.getCartItems(request)
        if request.method == 'POST':
            cart_item_id = int(request.POST['remove'])
            cartSession.removeCartItem(request, cart_item_id)
        cart_items = []
        cart_items_qty = 0
        total_price = 0
        for product_id, product_data in cart.items():
            product = get_object_or_404(Product, id=product_id)
            cart_items_qty += product_data['qty']
            total_price += product.price * product_data['qty']
            cart_items.append({
                'id': product_data['id'],
                'product': product,
                'quantity': product_data['qty'],
            })
    else:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        cart_items_qty = CartItem.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
        total_price = CartItem.get_total_price()
        if request.method == 'POST':
            cart_item_id = request.POST['remove']
            CartItem.objects.get(id=cart_item_id).delete()
    context = {
        'cart_items': cart_items,
        'quantitytotal': cart_items_qty,
        'totalprice': total_price,
    }
    return render(request, 'cart_list.html', context=context)
