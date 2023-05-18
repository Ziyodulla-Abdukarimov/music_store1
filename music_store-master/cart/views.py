from django.shortcuts import render


# Create your views here.
def cartList(request):
    return render(request, 'cart_list.html')
