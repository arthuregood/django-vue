import json
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer, TaxSerializer, TaxCalculatorSerializer
from .models import Product, Tax, TaxCalculator


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all().order_by('state')
    serializer_class = TaxSerializer


class CalculatorViewSet(viewsets.ModelViewSet):
    queryset = TaxCalculator.objects.all().order_by('date')
    serializer_class = TaxCalculatorSerializer

    def create(self, request):

        data = json.loads(request.body)

        response = {
            'products': [],
            'tax_value': int(data['tax_value']),
            'raw_value': 0,
            'total_value': 0
        }

        for product in data['products']:
            response['products'].append(product['name'])
            response['raw_value'] += float(product['value'])

        response['total_value'] = response['raw_value']
        if response['tax_value'] != 0:
            response['total_value'] += response['total_value'] * \
                (response['tax_value']/100)

        calculator = TaxCalculator(
            products=response['products'],
            tax_value=response['tax_value'],
            raw_value=response['raw_value'],
            total_value=response['total_value']
        )
        calculator.save()

        return Response(response)
