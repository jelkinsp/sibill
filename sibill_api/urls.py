from django.urls import path
from rest_framework.schemas import get_schema_view

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('invoice/', views.manage_invoice),
    path('invoice/<int:invoice_id>/', views.get_invoice_id),
    path('invoice/<str:user_name>/<int:year_invoice>/', views.get_invoice_average),
    path('openapi', get_schema_view(
        title="Sibill",
        description="Prueba tecnica",
        version="1.2.0"
    ), name='openapi-schema'),
]

