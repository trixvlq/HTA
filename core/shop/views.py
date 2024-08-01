from .tasks import checkout_cart
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import OrderForm
from .models import *


def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'title': 'Beer king',
    }
    return render(request, 'shop/index.html', context)


def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cart = request.cart
            email = request.POST.get('email')
            contact_data = request.POST.get('contact_data')
            address = request.POST.get('address')
            message = request.POST.get('message')
            total = 0
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                total += item.product.price * item.quantity
            messages = [
                f'Вы сделали заказ в {timezone.now()} на сумму ₸{total}'
                'Заказ состоит из:'
            ]
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                messages.append(
                    f'{item.product.name} - {item.quantity} шт. на сумму ₸{item.product.price * item.quantity}')

            mail_message = '\n'.join(messages)

            checkout_cart.delay(mail_message, email)

            mail_message = (f'Был сделан заказ в {timezone.now()} на сумму ₸{total}\n,'
                            f'Почта клиента: {email},\n'
                            f'Адрес доставки: {address},\n'
                            f'Контактные данные: {contact_data},\n'
                            f'Дополнительная информация: {message}'
                            f'Заказ состоит из:\n')

            checkout_cart.delay(mail_message)

            cart_items.delete()
            cart.updated_at = timezone.now()
            cart.save()
            return redirect('home')
    else:
        form = OrderForm(request.POST or None)
        cart = request.cart
        cart_items = CartItem.objects.filter(cart=cart)
        context = {
            'cart_items': cart_items,
            'title': 'Оформление заказа',
            'form': form
        }
        return render(request, 'shop/checkout.html', context)


def cart_view(request):
    cart_key = request.COOKIES.get('cart_key')
    cart = Cart.objects.get(key=cart_key) if cart_key else None
    cart_items = CartItem.objects.filter(cart=cart) if cart else []
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'cart_count': cart.cart_total_quantity() if cart else 0,
        'title': 'Корзина',
    }
    return render(request, 'shop/cart.html', context)


def category_view(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    context = {
        'products': products,
        'title': category.name,
    }
    return render(request, 'shop/index.html', context)


def add_to_cart(request, id):
    cart = request.cart
    product = Product.objects.get(id=id)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    cart.updated_at = timezone.now()
    cart.save()

    response = JsonResponse(
        {'cart_count': cart.cart_total_quantity(), 'product_count': cart_item.quantity, 'price': product.price})
    response.set_cookie('cart_key', cart.key, max_age=86400)

    return response


def cart_count(request):
    cart = request.cart
    return JsonResponse({'cart_count': cart.cart_total_quantity()})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return JsonResponse({'name': product.name, 'price': product.price})


def check_cart(request):
    cart = request.cart
    result = {

    }
    items = CartItem.objects.filter(cart=cart)
    for item in items:
        result[item.product.id] = item.quantity
    return JsonResponse(result)


def remove_from_cart(request, id):
    cart_key = request.COOKIES.get('cart_key')
    cart = Cart.objects.get(key=cart_key) if cart_key else None
    deleted = False
    if cart:
        product = get_object_or_404(Product, id=id)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            deleted = True
            cart_item.delete()

        cart.updated_at = timezone.now()
        cart.save()
        if deleted:
            response = JsonResponse(
                {'cart_count': cart.cart_total_quantity(), 'product_count': cart_item.quantity, 'deleted': True,
                 'price': cart_item.product.price})
        else:
            response = JsonResponse({'cart_count': cart.cart_total_quantity(), 'product_count': cart_item.quantity,
                                     'price': cart_item.product.price})
        return response
