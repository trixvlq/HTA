import uuid
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return str(self.key)

    def cart_total_price(self):
        return sum([item.product.price * item.quantity for item in self.items.all()])

    def cart_total_quantity(self):
        items = CartItem.objects.filter(cart=self)
        total = 0
        for item in items:
            total += item.quantity
        return total


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.cart)
