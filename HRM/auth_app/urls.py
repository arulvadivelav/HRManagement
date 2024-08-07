"""
    Auth module URL's
"""

from django.urls import path
from auth_app.rest_api import login

urlpatterns = [
    path("", login.login_page, name="login"),
]
