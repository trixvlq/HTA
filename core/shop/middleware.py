from django.utils.deprecation import MiddlewareMixin
from .models import Cart


class CartMiddleware(MiddlewareMixin):
    def process_request(self, request):
        cart_key = request.COOKIES.get('cart_key')
        if not cart_key:
            cart = Cart.objects.create()
            request.cart = cart
            request.new_cart = True
        else:
            try:
                cart = Cart.objects.get(key=cart_key)
                request.cart = cart
                request.new_cart = False
            except Cart.DoesNotExist:
                cart = Cart.objects.create()
                request.cart = cart
                request.new_cart = True

    def process_response(self, request, response):
        if hasattr(request, 'new_cart') and request.new_cart:
            response.set_cookie('cart_key', request.cart.key, max_age=86400)
        return response
