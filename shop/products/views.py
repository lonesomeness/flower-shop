from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from products.models import Product, Cart
from users.models import User


def index(request):
    return render(request, 'products/index.html')


def about(request):
    return render(request, 'products/about.html')


def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user)
    total_sum = cart.total_sum()
    context = {'cart': cart,
               'total_sum': total_sum
                }
    return render(request, 'products/cart.html', context)


@login_required
def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.filter(user=request.user, product=product)

    if not cart.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        cart = cart.first()
        cart.quantity += 1
        cart.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def create_order(request):
    user_cart = Cart.objects.filter(user=request.user)
    if user_cart.exists():
        order = user_cart.first().create_order()
        return HttpResponseRedirect(reverse('users:profile')) 
    return HttpResponseRedirect(reverse('products:cart'))  