from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from sibill_api.models import User, Product, Invoice
from sibill_api.serializers import UserSerializer, ProductSerializer, InvoiceSerializer


def invoice_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InvoiceSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
