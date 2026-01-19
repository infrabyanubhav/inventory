"""
This file contains the views for the inventory system.
"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.
# {


"""
The code is based on assuming that the inventory is stored in a database and the alerts are generated based on the inventory data. It is not a real-time system and the alerts are generated based on the inventory data.
"""


@api_view(["GET"])
def get_low_stock_alerts(request, company_id):
    """
    Get low stock alerts for a company.
    """
    try:

        # company = Company.objects.get(id=company_id)
        # if not company:
        # return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)
        alerts = [
            {
                "product_id": 123,
                "product_name": "Widget A",
                "sku": "WID-001",
                "warehouse_id": 456,
                "warehouse_name": "Main Warehouse",
                "current_stock": 5,
                "threshold": 20,
                "days_until_stockout": 12,
            }
        ]
        return Response({"alerts": alerts, "total_alerts": len(alerts)})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
