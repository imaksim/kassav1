from django.db import models
from django.core import validators


class Stuff(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "stuff"


class Products(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "products"


class PaymentMethods(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = "payment_methods"


class Operations(models.Model):
    date = models.DateTimeField(auto_now_add=True, )
    stuff_id = models.ForeignKey(Stuff, on_delete=models.SET_NULL, null=True)
    name_of_product_id = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    deb_cred = models.BooleanField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(validators=[validators.MinValueValidator(0)])
    total = models.DecimalField(max_digits=15, decimal_places=2, validators=[validators.MinValueValidator(0)])
    payment_id = models.ForeignKey(PaymentMethods, on_delete=models.SET_NULL, null=True)
    notice = models.TextField(null=True)

    class Meta:
        db_table = "Operations"
