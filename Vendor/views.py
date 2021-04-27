from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .form import *
from .filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib import messages
from .decorators import admin_only, authenticate_user, allowed_users

@authenticate_user
def home(request):
    return render(request, 'home.html')

@authenticate_user
def login_user(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Incorrect Credentials')
            
        
    return render(request, 'login.html')

@authenticate_user
def signup(request):          
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            
            Customer.objects.create(user=user, name=user.username, email=user.email)
            messages.success(request, 'Profile Created.')                          
            return redirect('login')
            
    value = {'form': form}    
    return render(request, 'signup.html', value)

@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url="login")
@admin_only
def dashboard(request):
    # print(request.user)
    orders = Order.objects.all()
    order_count = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out = orders.filter(status='Out for delivery').count()
    # products = Product.objects.all()
    customers = Customer.objects.all()
    index = customers.count()
    
    myfilter = Orderfilter2(request.GET, queryset=orders)
    orders = myfilter.qs
    # print(orders)
    # print(myfilter.form)
    value = {'orders': orders, 'customers': customers, 'order_count': order_count, 'delivered':delivered, 'pending': pending, 'out': out, 'myfilter': myfilter }

    return render(request, 'dashboard.html', value)

@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def products(request):
    products = Product.objects.all()
    value = {'products': products}
    return render(request, 'products.html', value)

@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_last5 = orders.reverse()[:5]
    order_count = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out = orders.filter(status='Out for delivery').count()
    
    myfilter = Orderfilter(request.GET, queryset=orders)
    orders = myfilter.qs
    value = {'orders': orders, 'customer': customer, 'order_count': order_count, 'delivered':delivered, 'pending': pending, 'out': out, 'last5': orders_last5, 'myfilter': myfilter }

    return render(request, 'customer.html', value)

@login_required(login_url="login")
def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm({'customer': customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/home')

            
    value = {'form': form, 'val': 'Create an Order:'}
    return render(request, 'create_form.html', value)
 
@login_required(login_url="login")    
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        form.save()
        return redirect('/home')
    value = {'form': form, 'val': 'Updating an Order:'}
    return render(request, 'create_form.html', value)

@login_required(login_url="login")
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/home')
        
    value = {'order': order}
    return render(request, 'delete.html', value)

@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        form.save()
        return redirect('/products')
    value = {'form': form, 'val': 'Updating an Product:'}
    return render(request, 'create_form.html', value)

@login_required(login_url="login")
@allowed_users(allowed_roles=['Admin'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('/products')
        
    value = {'order': product}
    return render(request, 'delete.html', value)

@allowed_users(allowed_roles=['Customer'])
def myprofile(request):   
    # print(request.user)
    customer = Customer.objects.get(user=request.user)
    # if customer.name == request.user:
    orders = customer.order_set.all()
    orders_last5 = orders.reverse()[:5]
    order_count = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out = orders.filter(status='Out for delivery').count()
    
    myfilter = Orderfilter(request.GET, queryset=orders)
    orders = myfilter.qs
    value = {'orders': orders, 'customer': customer, 'order_count': order_count, 'delivered':delivered, 'pending': pending, 'out': out, 'last5': orders_last5, 'myfilter': myfilter }

    return render(request, 'myprofile.html', value)

@login_required(login_url="login")    
@allowed_users(allowed_roles=['Customer'])
def updateprofile(request):
    customer = request.user.customer
    customer = Customer.objects.get(name=customer)
    user = User.objects.get(username=request.user)
    form = CustomerUpdate(instance=customer)
    if request.method == 'POST':
        form = CustomerUpdate(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            cus = form.save() 
            user.username = form.cleaned_data['name']
            user.save()
            return redirect('myprofile')
        
    value = {'form': form, 'customer': customer}
    return render(request, 'put_customer.html', value)

@login_required(login_url="login")    
@allowed_users(allowed_roles=['Customer'])
def placeorderCustomer(request):
    c = request.user
    customer = Customer.objects.get(name=c)
    form = OrderFormCustomer(instance=customer)
    if request.method == 'POST':
        form = OrderFormCustomer(request.POST)
        if form.is_valid():           
            new = form.save()
            new.customer = customer
            new.save()     
            return redirect('/home')

            
    value = {'form': form, 'val': 'Create an Order:'}
    return render(request, 'create_form.html', value)