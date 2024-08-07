from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from attendance.models import userAttendance
from datetime import timedelta, datetime
import json
import pytz


class AttendanceChart(View):
    def get(self, request):
        try:
            kolkata_tz = pytz.timezone("Asia/Kolkata")
            current_date = datetime.now(kolkata_tz).date()
            to_date = current_date - timedelta(days=1)
            from_date = current_date - timedelta(days=7)
            try:
                user_id = 2
                user_ref = User.objects.get(id=user_id)
            except User.DoesNotExist:
                messages.error(request, "User not found.")
                return HttpResponse("User not found.")

            date_list = []
            date = from_date
            while date <= to_date:
                date_list.append(date)
                date += timedelta(days=1)

            final_result = []
            for dat in date_list:
                data = {}
                attendance_details = userAttendance.objects.filter(
                    user_id=user_id, date=dat
                ).order_by("log_in")
                total_hours_per_date = 0
                for atten in attendance_details:
                    total_hours_per_date += (
                    atten.log_out - atten.log_in
                    ).total_seconds()
                data["date"] = dat.strftime("%Y-%m-%d")
                data["hours"] = round(total_hours_per_date / 3600, 2)
                final_result.append(data)

            attendance_details = userAttendance.objects.filter(
                    user_id=user_id, date__gte=from_date, date__lte=to_date
                )
            
            context = {
                "username": user_ref.first_name + " " + user_ref.last_name,
                "labels": [date["date"] for date in final_result],
                "log_in_times": [hour["hours"] for hour in final_result],
                "total_hours": [8 for _ in range(len(date_list))],
            }
            print(context)
            messages.success(request, "User attendance details provided successfully.")
            return render(request, "templates/attendance_chart.html", context)

        except Exception as e:
            print(e)
            messages.error(request, "Something went wrong. Please try again later.")
            return HttpResponse("Something went wrong.")


class AttendanceDetailsFilter(View):
    def post(self, request):
        try:
            try:
                data = json.loads(request.body)
                from_date = data.get("from_date")
                to_date = data.get("to_date")
                if from_date and to_date:
                    from_date = datetime.strptime(from_date, "%Y-%m-%d")
                    to_date = datetime.strptime(to_date, "%Y-%m-%d")

            except:
                messages.error(request, "Required fields are missing.")
                return HttpResponse("Required fields are missing.")

            try:
                user_id = 2
                user_ref = User.objects.get(id=user_id)
            except:
                messages.error(request, "User not found.")
                return HttpResponse("User not found.")

            if from_date and to_date:
                attendance_details = userAttendance.objects.filter(
                    user_id=user_id, date__gte=from_date, date__lte=to_date
                )
            else:
                kolkata_tz = pytz.timezone("Asia/Kolkata")

                to_date = datetime.now(kolkata_tz).date()
                from_date = to_date - timedelta(days=7)

                attendance_details = userAttendance.objects.filter(
                    user_id=user_id, date__gte=from_date, date__lte=to_date
                )

            date_list = []
            date = from_date
            while date <= to_date:
                date_list.append(date)
                date += timedelta(days=1)

            final_result = []
            for dat in date_list:
                data = {}
                attendance_details = userAttendance.objects.filter(
                    user_id=user_id, date=dat
                ).order_by("log_in")
                total_hours_per_date = 0
                for atten in attendance_details:
                    total_hours_per_date += (
                    atten.log_out - atten.log_in
                    ).total_seconds()
                data["date"] = dat.strftime("%Y-%m-%d")
                data["hours"] = round(total_hours_per_date / 3600, 2)
                final_result.append(data)

            attendance_details = userAttendance.objects.filter(
                    user_id=user_id, date__gte=from_date, date__lte=to_date
                )
            
            context = {
                "username": user_ref.first_name + " " + user_ref.last_name,
                "labels": [date["date"] for date in final_result],
                "log_in_times": [hour["hours"] for hour in final_result],
                "total_hours": [8 for _ in range(len(date_list))],
            }
            print(context)
            return JsonResponse(context)

        except Exception as e:
            print(e)
            return JsonResponse(
                {"error": "Something went wrong. Please try again later."}, status=500
            )
