from django.urls import path
from .views import invoice_list

urlpatterns = [

    path('invoice/', invoice_list),
]
