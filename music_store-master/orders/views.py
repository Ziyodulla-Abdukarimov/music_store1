from django.shortcuts import render
from models.models import Category
from canfigure import title


# Create your views here.
def checkout(request):
    return render(request, 'checkout.html', {
        'categories': Category.objects.filter(parent=None),
        'store_title': title
    })
