from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic

from .models import Order, Order_line, Shop, Product

# views file

def shop(request, shop_id):
	return HttpResponse("you're looking at shop %s." % shop_id)


def index(request):
	return HttpResponse("index page")

class OrderListView(generic.ListView):
    model = Order
    ordering = ['order_date', 'shop']
    template_name = 'order/order_list.html'
    paginate_by = 15

def order_detail(request, order_id):
	return HttpResponse("you're looking at order %s." % order_id)

class OrderDetailView(generic.DetailView):
    model = Order

def order_line_create(request, pk):
    """
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = CurrencyConvertForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            base = form.cleaned_data['base']
            target = form.cleaned_data['target']
            amount = form.cleaned_data['base_amount']
        
            # process Fixer API request:
            data = do_conversion(base, target, amount)
            context = {}
            context['base'] = base
            context['target'] = target
            context['amount'] = amount 
            context['rate'] = data['rate']
            context['result'] = data['result']

            # redirect to a new URL:
            return render(request, 'currency/convert_result.html', context=context)

    # If this is a GET (or any other method) create the default form.
    else:
        form = CurrencyConvertForm(initial={'base': 'EUR', 'target': 'USD'})

    context = {
        'form': form,
    }
    return render(request, 'currency/convert_form.html', context)
    """
    order = Order.objects.get(pk=pk)
    return HttpResponse("you're creating new order line for %s - %s." % (order.shop.name, order.order_date))




