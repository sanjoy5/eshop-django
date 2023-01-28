from django.urls import path
from .views import *

urlpatterns = [
    path('category/<int:id>/<slug:slug>/',category_products,name="category_products"),
    path('product/<int:id>/<slug:slug>/',product_details,name="product_details"),
    path('search/',search,name='search'),
    path('search_auto/',search_auto,name='search_auto'),


    path('product/addcomment/<int:id>/',addcomment,name='addcomment'),
]
