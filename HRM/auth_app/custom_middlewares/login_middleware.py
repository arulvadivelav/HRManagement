from django.shortcuts import render
from django.contrib import messages
from HRM.settings import EXCEPTION_URLS


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.process_request(request)
        if response:
            return response
        response = self.get_response(request)
        return response

    def process_request(self, request):
        if not request.user.is_authenticated and request.path not in EXCEPTION_URLS:
            messages.warning(request, "Log in Required")
            return render(request, "templates/login.html")
