"""
This file contains the urls for the inventory system.
"""
from django.urls import path

from .views import get_low_stock_alerts


urlpatterns = [
    path("companies/<int:company_id>/alerts/low-stock", get_low_stock_alerts, name="get_low_stock_alerts"),
]
