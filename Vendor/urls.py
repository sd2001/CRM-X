from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),    
    path('login/', views.login_user, name="login"),    
    path('signup/', views.signup, name="signup"),    
    path('logout/', views.logout_user, name="logout"),    
    path('home/', views.dashboard, name="dashboard"),
    path('products/', views.products,name="products"),
    path('customers/<str:pk>', views.customer, name="customer"),
    path('createOrder/<str:pk>', views.createOrder, name="createOrder"),
    path('updateOrder/<str:pk>', views.updateOrder, name="updateOrder"),
    path('deleteOrder/<str:pk>', views.deleteOrder, name="deleteOrder"),
    path('updateProduct/<str:pk>', views.updateProduct, name="updateProduct"),
    path('deleteProduct/<str:pk>', views.deleteProduct, name="deleteProduct"),
]