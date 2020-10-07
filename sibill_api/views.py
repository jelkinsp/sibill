from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework import status

from sibill_api.models import User, Product, Invoice
from sibill_api.serializers import UserSerializer, ProductSerializer, InvoiceSerializer


@api_view(['POST', 'DELETE'])
def manage_invoice(request):
    data = JSONParser().parse(request)
    if request.method == 'POST':
        try:
            user_invoice = User.objects.get(id=data['user_id'])
        except User.DoesNotExist:
            return Response("User not exict", status=status.HTTP_404_NOT_FOUND)
        try:
            for product in data["products"]:
                Product.objects.get(id=product)
        except Product.DoesNotExist:
            return Response("Product  not exict", status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceSerializer(data={"products": data["products"]})
        # Falta coger el id de la factura y relacionarla con el Usuario
        if serializer.is_valid():
            serializer.save()
            user_invoice.invoices.add(serializer.data['id'])
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        try:
            invoice = Invoice.objects.get(id=data["id"])
        except Invoice.DoesNotExist:
            return Response("Invoice not exict", status=status.HTTP_404_NOT_FOUND)
        invoice.delete()
        return Response(status=200)


@api_view(['GET'])
def get_invoice_id(request, invoice_id):
    if request.method == 'GET':
        try:
            invoice = Invoice.objects.get(id=invoice_id)
        except Invoice.DoesNotExist:
            return Response("Invoice {} not exict".format(invoice_id), status=status.HTTP_404_NOT_FOUND)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def get_invoice_average(request, user_name, year_invoice):
    if request.method == 'GET':
        try:
            invoice = Invoice.objects.filter(date_invoice__year=year_invoice, user__name=user_name)  # Query
        except Invoice.DoesNotExist:
            return Response("Username or Year not exict", status=status.HTTP_404_NOT_FOUND)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data, status=200)
