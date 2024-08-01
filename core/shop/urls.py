from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('category/<int:id>/', category_view, name='category'),
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
    path('cart_count/', cart_count, name='cart_count'),
    path('check_cart/', check_cart, name='check_cart'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('remove_from_cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
]
