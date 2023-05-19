from django.shortcuts import render
from cart.cart import CartItem, UserCart
from django.db.models import Sum, F


# Create your views here.
def cartList(request):
    if request.method == 'POST':
        cart_item_id = request.POST['remove']
        CartItem.objects.get(id=cart_item_id).delete()
    context = {
        'cart_items': CartItem.objects.filter(cart__user=request.user),
        'quantitytotal': CartItem.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0,
        'totalprice': CartItem.objects.annotate(item_price=F('product__price') * F('quantity')).aggregate(
            total_price=Sum('item_price'))['total_price'] or 0,
    }
    return render(request, 'cart_list.html', context=context)
