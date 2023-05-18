from django.urls import path
from .views import dashboard, product_detail, category_detail, contact
from cart.views import cartList

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('contact/', contact, name='contact'),
    path('product/<int:pk>/', category_detail, name='product'),
    path('product/<int:pk>/<int:id>', product_detail, name='product_detail'),
    path('cart-list/', cartList, name='cartList'),
]
