from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)


class Invoice(models.Model):
    street ="calle"
    way = "camino"
    avenue = "avenida"
    type_choices = [
        (street, "calle"),
        (way, "camino"),
        (avenue, "avenida"),
    ]

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    date_invoice = models.DateField(auto_now_add=True)
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
    iva = models.DecimalField(max_digits=5, decimal_places=2)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
