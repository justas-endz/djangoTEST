from django.db import models
from django.conf import settings

CATEGORY = (
    ('SHR', 'Špižinis Radiatorius'),
    ('MR', 'Metalinis Radiatorius'),
    ('ER', 'Elektrinis Radiatorius')
)
STATUS_NAME = (
    ('O', 'ORDERED'),
    ('SH', 'SHIPPED'),
    ('DE', 'DELIVERED'),
)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.last_name

    def register(self):
        self.save()


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.CharField(choices=CATEGORY, max_length=3)
    product_quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product_name)


class ProductOrder(models.Model):
    product_id = models.ForeignKey(Product, verbose_name="Product", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.product_id)


class Status(models.Model):
    status_name = models.CharField(choices=STATUS_NAME, max_length=2)

    def __str__(self):
        return self.status_name


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, verbose_name="User", on_delete=models.SET_NULL, null=True, blank=True)
    ordered_date = models.DateTimeField()
    status_id = models.ForeignKey(Status, verbose_name="Status", on_delete=models.SET_NULL, null=True, blank=True)
    product_id = models.ForeignKey(Product, verbose_name="Product", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.product_id)
