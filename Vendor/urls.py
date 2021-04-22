from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products,name="products"),
    path('customers/<str:pk>', views.customer, name="customer")
]