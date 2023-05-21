from django.contrib import admin
from .models import Order, OrderItems


class OrderInline(admin.TabularInline):
    model = OrderItems
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline]


admin.site.register(Order, OrderAdmin)
