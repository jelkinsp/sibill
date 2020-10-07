from django.urls import path
from . import views

urlpatterns = [

    path('invoice/', views.manage_invoice ),
    path('invoice/<int:invoice_id>/', views.get_invoice_id),
    path('invoice/<str:user_name>/<int:year_invoice>/', views.get_invoice_average),
]
