from django.contrib import admin
from .models import Tax, Product, TaxCalculator

admin.site.register(Tax)
admin.site.register(Product)
admin.site.register(TaxCalculator)
