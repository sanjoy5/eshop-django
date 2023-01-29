from django.urls import path
from .views import *


urlpatterns = [
    path('login/',loginPage,name='login'),
    path('signup/',signupPage,name='signup'),
    path('logout/',logOutPage,name='logout'),
    
    path('user/',UserPage,name="user"),


]
