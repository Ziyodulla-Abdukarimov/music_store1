from django.contrib import admin
from cart.models import UserCart, CartItem
from .models import Category, Product


# Register your models here.
class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(UserCart)
admin.site.register(CartItem)
admin.site.register(Product)
