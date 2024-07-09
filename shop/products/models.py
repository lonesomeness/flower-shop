from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products_images')

    def __str__(self):
        return f"Продукт: {self.name}"
    
    
class CartQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(user_cart.sum() for user_cart in self)
    
    def total_quantity(self):
        return sum(user_cart.quantity for user_cart in self)


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт: {self.product.name}'
    
    def sum(self):
        return self.product.price * self.quantity
    
    def create_order(self):
        total_amount = self.sum()
        order = Order.objects.create(user=self.user, total_amount=total_amount)
        self.delete()
        return order

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Заказ {self.id} | Пользователь: {self.user.username}'


    
