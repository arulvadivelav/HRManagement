from django.urls import path
from attendance.rest_api import attendance_details, attendance_login

urlpatterns = [
    path(
        "attendance_login_index",
        attendance_login.attendance_login_indexpage,
        name="attendance_login_index",
    ),
    path(
        "attendance_login",
        attendance_login.AttendanceLogin.as_view(),
        name="attendance_login",
    ),
    path(
        "attendance_detail",
        attendance_details.AttendanceChart.as_view(),
        name="attendance_detail",
    ),
    path(
        "attendance_detail_with_datefilter",
        attendance_details.AttendanceDetailsFilter.as_view(),
        name="attendance_detail_with_datefilter",
    ),
]
