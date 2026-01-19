"""
This file contains the tests for the inventory system.
"""
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

# Create your tests here.


class CompanyApiTestCase(TestCase):
    """
    Test case for the Company API.
    """
    def setUp(self):
        self.client = APIClient()
    def test_get_companies(self):
        response = self.client.get(reverse("get_low_stock_alerts", kwargs={"company_id": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["total_alerts"], len(response.data["alerts"]))
        
        