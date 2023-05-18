from models.models import Category
from canfigure import title


def base_context(request):
    return {
        'categories': Category.objects.filter(parent=None), 'store_title': title}
