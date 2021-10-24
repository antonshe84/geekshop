from django.db import models
from django.db.models import Sum
from users.models import Users
from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'корзина для {self.user.username}| Товар {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    @classmethod
    def total_quantity(cls):
        res = cls.objects.all().aggregate(Sum('quantity'))
        return res['quantity__sum']

    @classmethod
    def total_sum(cls):
        data = cls.objects.all()
        res = 0
        for i in data:
            res += i.sum()
        return res
