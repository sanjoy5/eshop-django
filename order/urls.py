from django.urls import path
from .views import *

urlpatterns = [
    path('order/addtocart/<int:id>/',addToCart,name='addtocart'),
    path('order/deletefromcart/<int:id>/',deletefromcart,name='deletefromcart'),
    path('shopcart/',shopCart,name='shopcart'),
    path('order/orderproduct/',orderProduct,name='orderproduct'),
]
