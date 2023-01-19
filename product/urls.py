from django.urls import path
from .views import *

urlpatterns = [
    path('category/<int:id>/<slug:slug>/',category_products,name="category_products"),
    path('search/',search,name='search'),
    path('search_auto/',search_auto,name='search_auto'),
]
