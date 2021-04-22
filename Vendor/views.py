from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    orders = Order.objects.all()
    order_count = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out = orders.filter(status='Out for delivery').count()
    # products = Product.objects.all()
    customers = Customer.objects.all()
    index = customers.count()
    value = {'orders': orders, 'customers': customers, 'order_count': order_count, 'delivered':delivered, 'pending': pending, 'out': out }

    return render(request, 'dashboard.html', value)

def products(request):
    products = Product.objects.all()
    value = {'products': products}
    return render(request, 'products.html', value)

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_last5 = orders.reverse()[:5]
    order_count = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out = orders.filter(status='Out for delivery').count()
    value = {'orders': orders, 'customer': customer, 'order_count': order_count, 'delivered':delivered, 'pending': pending, 'out': out, 'last5': orders_last5 }

    return render(request, 'customer.html', value)
    
    