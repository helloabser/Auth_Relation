from django.urls import path
from .views import *
urlpatterns = [
    path('register/',registerPage, name='register'),
    path('',loginPage, name='login'),
    path('dashboard/',dashboardPage, name='dashboard'),
    path('addProduct/',addProductPage, name='addProduct'),
    path('orderList/',orderListPage, name='orderList'),
    path('orderPage/<int:id>/',orderPage, name='orderPage'),
]