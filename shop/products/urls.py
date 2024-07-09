from django.urls import path, include
from products import views 

app_name = 'products'

urlpatterns = [
path('', views.products, name='index'),
path('cart/', views.cart, name='cart'),
path('cart/add/<int:product_id>', views.cart_add, name='cart_add'),
path('cart/remove/<int:cart_id>', views.cart_remove, name='cart_remove'),
path('cart/create_order/', views.create_order, name='create_order'),
]