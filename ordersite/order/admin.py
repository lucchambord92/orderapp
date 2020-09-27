from django.contrib import admin

# Register your models here.

from .models import Shop, Product, Order, Order_line

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_line)
