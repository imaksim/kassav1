from django.contrib import admin

# Register your models here.
from .models import Stuff, Products, PaymentMethods, Operations, Sales

admin.site.register(Stuff)
admin.site.register(Products)
admin.site.register(PaymentMethods)
admin.site.register(Operations)
admin.site.register(Sales)