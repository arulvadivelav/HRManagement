from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from admin_pannel.models import UserLookUp
import json, pytz, traceback
from attendance.models import userAttendance
from datetime import datetime


def attendance_login_indexpage(request):
    user_id = 2  # Use request.user.id in a real scenario
    try:
        user_log_status = UserLookUp.objects.get(user_id=user_id)
    except UserLookUp.DoesNotExist:
        messages.error(request, "User not found.")
        return HttpResponse("User not found.")

    context = {"user_log_status": False if user_log_status.log_status else True}
    return render(request, "attendance_login_logout.html", context)


class AttendanceLogin(View):
    def post(self, request):
        try:
            try:
                data = json.loads(request.body)
                log_status = data.get("log_status")
            except:
                messages.error(request, "Required fields are missing.")
                return HttpResponse("Required fields are missing.")

            user_id = 2  # request.user.id
            try:
                user_ref = User.objects.get(id=user_id)
            except:
                messages.error(request, "User not found.")
                return HttpResponse("User not found.")

            # Update the user lookup to ensure the status
            user_log_status = UserLookUp.objects.filter(user_id=user_id).update(
                log_status=log_status
            )
            # add timein timeout details to calculate the hours
            kolkata_tz = pytz.timezone("Asia/Kolkata")
            current_date = datetime.now(kolkata_tz).date()
            current_datetime = datetime.now(kolkata_tz)
            if log_status:
                add_login = userAttendance.objects.create(
                    user_id=user_id, date=current_date, log_in=current_datetime
                )
                messages.success(request, "Failed to download video.")
                return JsonResponse({"data": "success"})
            else:
                add_logout = userAttendance.objects.filter(
                    user_id=user_id, date=current_date, log_out=None
                ).update(log_out=current_datetime)
                messages.success(request, "Failed to download video.")
                return JsonResponse({"data": "success"})

        except Exception as e:
            print(e)
            traceback.print_exc()
            return JsonResponse(
                {"error": "Something went wrong. Please try again later."}, status=500
            )
