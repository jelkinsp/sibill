from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)


class Invoice(models.Model):
    date_invoice = models.DateField()
    iva = models.DecimalField(max_digits=5, decimal_places=2, default="21")
    products = models.ForeignKey(Product, on_delete=models.CASCADE)


class User(models.Model):
    street = "cl"
    way = "cm"
    avenue = "av"
    type_choices = [
        (street, "calle"),
        (way, "camino"),
        (avenue, "avenida"),
    ]
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    dni = models.CharField(max_length=9)
    address = models.CharField(max_length=50)
    number = models.IntegerField()
    address_type = models.CharField(
        choices=type_choices,
        default=street,
        max_length=7
    )
    location = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    invoices = models.ForeignKey(Invoice, on_delete=models.CASCADE)
