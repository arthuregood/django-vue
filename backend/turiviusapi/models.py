from django.db import models
from django.contrib.auth.models import User
import datetime


class Tax(models.Model):
    state = models.CharField(max_length=20, default='')
    value = models.IntegerField('Value', default=0)


class Product(models.Model):
    name = models.CharField(max_length=20, default='')
    value = models.DecimalField(
        'Value', default=0, max_digits=10, decimal_places=2)


class TaxCalculator(models.Model):
    date = models.DateField('Date', default=datetime.date.today)
    products = models.JSONField('products', null=True)
    tax_value = models.IntegerField('Tax Value', default=0)
    raw_value = models.DecimalField(
        'Brute Value', default=0, max_digits=10, decimal_places=2)
    total_value = models.DecimalField(
        'Total Value', default=0, max_digits=10, decimal_places=2)
