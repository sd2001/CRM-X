from django.contrib import admin
from django.contrib.auth import views as auth_views
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
    path('myprofile/', views.myprofile, name="myprofile"),
    path('updateProfile/', views.updateprofile, name="updateprofile"),
    path('placeorder/', views.placeorderCustomer, name="placeorder"),
    path('createOrder/<str:pk>', views.createOrder, name="createOrder"),
    path('updateOrder/<str:pk>', views.updateOrder, name="updateOrder"),
    path('deleteOrder/<str:pk>', views.deleteOrder, name="deleteOrder"),
    path('updateProduct/<str:pk>', views.updateProduct, name="updateProduct"),
    path('deleteProduct/<str:pk>', views.deleteProduct, name="deleteProduct"),
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]