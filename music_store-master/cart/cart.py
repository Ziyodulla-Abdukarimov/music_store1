from models.models import Product
from django.shortcuts import get_object_or_404
from .models import UserCart, CartItem
from config import settings


class CartSession:
    def cartAddSession(self, request, qty, id):
        if request.user.is_authenticated:
            user_cart, _ = UserCart.objects.get_or_create(user=request.user, cart_id_pk=settings.CART_SESSION_ID)
            cart_item, created = CartItem.objects.get_or_create(
                product_id=id,
                cart=user_cart,
                defaults={'quantity': qty}
            )

            if not created:
                cart_item.quantity += qty
                cart_item.save()
        else:
            product_document = {
                'id': id,
                'name': get_object_or_404(Product, id=id).name,
                'qty': qty
            }
            session_cart = request.session.get('cart', {})
            existing_product = session_cart.get(str(id))

            if existing_product:
                existing_product['qty'] += qty
            else:
                session_cart[str(id)] = product_document

            request.session['cart'] = session_cart
            request.session.save()

    def removeCartItem(self, request, id):

        session_cart = request.session.get('cart', {})
        if str(id) in session_cart:
            del session_cart[str(id)]
            request.session['cart'] = session_cart
            request.session.save()

    def getCartItems(self, request):
        return request.session.get('cart', {})
