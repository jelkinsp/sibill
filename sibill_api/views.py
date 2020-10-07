from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status

from sibill_api.models import User, Product, Invoice
from sibill_api.serializers import UserSerializer, ProductSerializer, InvoiceSerializer


# @api_view(['GET', 'POST'])
# def invoice_list(request):
#     if request.method == 'GET':
#         invoices = Invoice.objects.all()
#         serializer = InvoiceSerializer(invoices, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = InvoiceSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


class InvoiceAPIView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        try:
            user_invoice = User.objects.get(id=data['user_id'])
        except User.DoesNotExist:
            return Response("User not exict", status=status.HTTP_404_NOT_FOUND)
        try:
            for product in data["products"]:
                Product.objects.get(id=product)
        except Product.DoesNotExist:
            return Response("Product id={} not exict".format(product), status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceSerializer(data={"products": data["products"]})
        # Falta coger el id de la factura y relacionarla con el Usuario

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, invoice_id):
        try:
            invoice = Invoice.objects.get(id=invoice_id)
        except Invoice.DoesNotExist:
            return Response("Invoice {} not exict".format(invoice_id), status=status.HTTP_404_NOT_FOUND)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data, status=200)

    def get(self, request):
        try:
            invoice = Invoice.objects.filter()
        except Invoice.DoesNotExist:
            return Response("Invoice {} not exict".format(id), status=status.HTTP_404_NOT_FOUND)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data, status=200)

    def delete(self, request):
        data = JSONParser().parse(request)
        try:
            invoice = Invoice.objects.get(id=data["id"])
        except Invoice.DoesNotExist:
            return Response("Invoice not exict", status=status.HTTP_404_NOT_FOUND)
        invoice.delete()
        return Response(status=200)
