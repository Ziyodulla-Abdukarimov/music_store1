from django.shortcuts import render, redirect, get_object_or_404
from .models import MyUser
from django.contrib import messages
from .utilites import validate_phone_number, validate_email
from django.contrib.auth import authenticate, login as authlogin, logout
from config import settings
from cart.models import UserCart, CartItem
from models.models import Product


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not validate_email(email):
            messages.error(request, 'Email is invalid 🤐')
            return redirect('register')
        if not validate_phone_number(phone):
            messages.error(request, "Phone number is invalid 🤐")
            return redirect('register')
        if password == password2:
            if not MyUser.objects.filter(username=username).exists():
                MyUser.objects.create_user(username=username, email=email, phone_number=phone, password=password)
            else:
                messages.error(request, "Username is already used 😆")
                redirect('register')
        else:
            messages.error(request, 'password is not the same')
    return render(request, 'account/register.html')


def login(request):
    if request.method == 'POST':
        email_username = request.POST['email_username']
        password = request.POST['password']
        user = authenticate(request, username=email_username, password=password)
        if user is not None:
            authlogin(request, user)
            if len(request.session.get('cart', {})) > 0:
                cart = request.session[settings.CART_SESSION_ID]
                user_cart, _ = UserCart.objects.get_or_create(user=user, cart_id_pk=settings.CART_SESSION_ID)

                for item, item_data in cart.items():
                    product = get_object_or_404(Product, id=item_data['id'])
                    cart_item = CartItem(cart=user_cart, product=product, quantity=item_data['qty'])
                    cart_item.save()

            if str(user.user_role) == 'client':
                return redirect('dashboard')

    return render(request, 'account/login.html')
