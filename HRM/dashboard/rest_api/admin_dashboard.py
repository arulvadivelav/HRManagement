"""

This file contain Admin dashboard API logics

"""

from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
import json


def admin_dashboard(request):
    return render(request, "templates/admin_dashboard.html")
