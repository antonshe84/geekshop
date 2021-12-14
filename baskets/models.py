from django.db import models
from django.db.models import Sum
from users.models import Users
from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='baskets')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'корзина для {self.user.username}| Товар {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    @property
    def baskets(self):
        return Basket.objects.filter(user=self.user)

    def total_quantity(self):
        return sum(basket.quantity for basket in self.baskets)  # baskets, который property

    def total_sum(self):
        return sum(basket.sum() for basket in self.baskets)  # baskets, который property
