from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .form import *

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

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    value = {'form': form, 'val': 'Create an Order:'}
    return render(request, 'create_form.html', value)
    
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        form.save()
        return redirect('/')
    value = {'form': form, 'val': 'Updating an Order:'}
    return render(request, 'create_form.html', value)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
        
    value = {'order': order}
    return render(request, 'delete.html', value)

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        form.save()
        return redirect('/products')
    value = {'form': form, 'val': 'Updating an Product:'}
    return render(request, 'create_form.html', value)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('/products')
        
    value = {'order': product}
    return render(request, 'delete.html', value)
    
    