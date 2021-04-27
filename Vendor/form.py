from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
        # exclude = ['customer']

class OrderFormCustomer(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderFormCustomer, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)      
        self.fields['status'].disabled = True        
        # self.fields['customer'].disabled = True        
    class Meta:
        model = Order
        # fields = ['product']
        fields = '__all__'
        exclude = ['customer']
        
        
        
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class CustomerUpdate(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
    