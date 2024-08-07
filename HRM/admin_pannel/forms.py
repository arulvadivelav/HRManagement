"""
Forms for 

"""

from django import forms
from django.contrib.auth.models import User


class UserStatusUpdate(forms.Form):
    is_active = forms.BooleanField()
