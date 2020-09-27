import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Order, Order_line, Product


class OrderLineForm(forms.Form):
    product = forms.ChoiceField(choices=[(f"{p.name} {p.format}", p) for p in Product.objects.all()])
    quantity = forms.IntegerField()
    unit_price = forms.DecimalField(max_digits=10, decimal_places=2)
    reduction_rate = forms.IntegerField(blank=True,null=True)
    reduction_rate_no_prod = forms.IntegerField(blank=True,null=True)
    no_buy = forms.IntegerField(blank=True,null=True)
    no_free = forms.IntegerField(blank=True,null=True)
    



