from django.db import models

import datetime

class Shop(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    format = models.CharField(max_length=30)
    type = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}-{self.format}"
    
class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_date = models.DateField()

    def __str__(self):
        return f"{self.shop.name}-{self.order_date}"

class Order_line(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    reduction_type = models.IntegerField(blank=True,null=True)
    reduction_rate = models.IntegerField(blank=True,null=True)
    reduction_rate_no_prod = models.IntegerField(blank=True,null=True)
    no_buy = models.IntegerField(blank=True,null=True)
    no_free = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return f"{self.order}-{self.product}"
