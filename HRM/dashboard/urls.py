"""
    Dashboard pannel URL's
"""

from django.urls import path
from dashboard.rest_api import admin_dashboard

urlpatterns = [
    path("", admin_dashboard.admin_dashboard, name="admin_dashboard"),
]
