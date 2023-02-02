from decimal import Decimal
from django.db import models
from Shop.models import Product
# Create your models here.


class Order(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    addresse = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    update_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    def get_total_cost(self):
        total_cost = sum(Decimal(item.get_cost() for item in self.items.all()))
        return total_cost


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
