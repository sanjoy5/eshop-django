from django.urls import path
from .views import *


urlpatterns = [
    path('login/',loginPage,name='login'),
    path('signup/',signupPage,name='signup'),
    path('logout/',logOutPage,name='logout'),
    
    path('user/',UserPage,name="user"),
    path('user/update',user_update,name="user_update"),
    path('user/password',user_password,name="user_password"),
    path('user/orders',user_orders,name="user_orders"),
    path('user/orderdetail/<int:id>/',user_orderdetail,name="user_orderdetail"),
    path('user/orders_product',user_order_product,name="user_order_product"),
    path('user/order_product_detail/<int:id>/<int:oid>/',
         user_order_product_detail, name='user_order_product_detail'),
]
