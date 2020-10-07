from sibill_api.models import User, Product, Invoice
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']


class InvoiceSerializer(serializers.ModelSerializer):
    # products = ProductSerializer()

    class Meta:
        model = Invoice
        fields = '__all__'

    # def create(self, validated_data):
    #     products_data = validated_data.pop('products')
    #
    #     invoice = Invoice.objects.create(**validated_data)
    #     Product.objects.create(invoice=invoice, **products_data)
    #     return invoice


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'surname', 'dni', 'address', 'number', 'address_type', 'location', 'province', 'invoices']
