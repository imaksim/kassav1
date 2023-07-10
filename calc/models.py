from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core import validators




class Stuff(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "stuff"
        ordering = ["-id"]
    def __str__(self):
        return f"{self.name}"

class Products(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "products"

    def __str__(self):
        return f"{self.id})  {self.name}"


class CreditProducts(Products):
    class Meta:
        verbose_name = "Credit Product"
        verbose_name_plural = "Credit Products"
        db_table = "credit_products"


class PaymentMethods(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = "payment_methods"
    def __str__(self):
        return f"{self.name}"




class Operations(models.Model):
    # fk_credit_product = models.ForeignKey(CreditProducts, on_delete=models.PROTECT, null=True)
    # fk_name_of_product = models.ForeignKey(Products, on_delete=models.PROTECT, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(validators=[validators.MinValueValidator(0)])
    def __str__(self):
        return f"{self.content_object.name}"
    class Meta:
        db_table = "operations"





class Sales(models.Model):
    sell_id = models.IntegerField(validators=[validators.MinValueValidator(0)])
    date = models.DateTimeField(auto_now_add=True)
    fk_stuff = models.ForeignKey(Stuff, on_delete=models.PROTECT, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, validators=[validators.MinValueValidator(0)])
    fk_payment = models.ForeignKey(PaymentMethods, on_delete=models.PROTECT, null=True)
    notice = models.TextField(null=True)

    class Meta:
        db_table = "sales"
    def __str__(self):
        return f"""{self.date.strftime("%Y-%m-%d %H:%M:%S")}"""
