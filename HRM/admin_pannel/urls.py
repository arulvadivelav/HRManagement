"""
    Admin pannel URL's
"""

from django.urls import path
from admin_pannel.rest_api import users

urlpatterns = [
    # path("users_index_page", users.UsersList.as_view(), name="users_index_page"),
    path("users", users.UsersList.as_view(), name="users"),
    path(
        "update_user_status/<int:user_id>",
        users.UpdateUser.as_view(),
        name="update_user_status",
    ),
]
