"""

This file contains all the admin related API logics

"""

from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
import json


class UsersList(View):
    def get(self, request):
        try:
            if request:  # request.user.is_superuser
                search_value = request.GET.get(
                    "search_value", ""
                )  # Get search value from query params
                if search_value:
                    user_details = (
                        User.objects.filter(username__icontains=search_value)
                        .exclude(is_superuser=True)
                        .order_by("id")
                    )
                else:
                    user_details = (
                        User.objects.all().exclude(is_superuser=True).order_by("id")
                    )
                count = 1
                users_list = []
                for user in user_details:
                    data = {}
                    name = f"{user.first_name or ''} {user.last_name or ''}".strip()
                    data["sno"] = count  # This is for UI purpose only
                    data["id"] = user.id
                    data["name"] = name if name else ""
                    data["username"] = user.username
                    data["email"] = user.email
                    data["is_active"] = user.is_active
                    users_list.append(data)
                    count += 1

                messages.success(request, "User details provided successfully.")
                return render(
                    request, "templates/user_details.html", {"user_details": users_list}
                )

            else:
                messages.error(request, "Failed to download video.")
                return HttpResponse("error")

        except Exception as e:
            print(e)
            messages.error(request, "Something went wrong Please try again later.")
            return HttpResponse("Something went wrong.")


class UpdateUser(View):
    def put(self, request, user_id):
        try:
            if request:  # request.user.is_superuser
                try:
                    data = json.loads(request.body)
                    is_active = data.get("is_active")
                except:
                    messages.error(request, "Required fields are missing.")
                    return HttpResponse("Required fields are missing.")
                try:
                    user_ref = User.objects.get(id=user_id)
                except:
                    messages.error(request, "User not found.")
                    return HttpResponse("User not found.")

                user_ref.is_active = is_active
                user_ref.save()

                messages.success(request, "User details provided successfully.")
                return HttpResponse("User status updated successfully.")

            else:
                messages.error(request, "Failed to download video.")
                return HttpResponse("error")

        except Exception as e:
            print(e)
            messages.error(request, "Something went wrong Please try again later.")
            return HttpResponse("error")
