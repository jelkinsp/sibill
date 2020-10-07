from django.urls import path
from .views import InvoiceAPIView

urlpatterns = [

    path('invoice/', InvoiceAPIView.as_view()),
    path('invoice/<int:id>', InvoiceAPIView.as_view()),
]
