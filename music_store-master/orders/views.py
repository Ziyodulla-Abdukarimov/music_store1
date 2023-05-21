from django.shortcuts import render, redirect
from canfigure import bot_token, admin_id
from .models import Order
from cart.cart import CartItem
from common.validators import validate_email
from django.contrib import messages
from common.telegram import send_message


def checkout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            cardholder = request.POST['card-holder']
            card_no = request.POST['card-no']
            credit_expiry = request.POST['credit-expiry']
            credit_cvc = request.POST['credit-cvc']
            billing_address = request.POST['billing-address']
            billing_zip = request.POST['billing-zip']
            send_message(bot_token, str(admin_id), email)

            if not validate_email(email):
                messages.error(request, 'Email is invalid 🤐')
            else:
                try:
                    order = Order.objects.create(
                        user=request.user,
                        email=email,
                        cardHolder=cardholder,
                        cardNo=card_no,
                        creditExpiry=credit_expiry,
                        creditCvc=credit_cvc,
                        billingAddress=billing_address,
                        billingZip=billing_zip,
                        totalPrice=CartItem.get_total_price(),
                    )
                    order.cart_items.set(CartItem.objects.all())
                    CartItem.objects.all().delete()
                except Exception as e:
                    messages.error(request, f"Failed to create order: {str(e)}")

    else:
        return redirect('login')

    return render(request, 'checkout.html')


def my_orders(request):
    context = {
        'order': Order.objects.get(user=request.user)
    }
    return render(request, 'myorders.html', context)
