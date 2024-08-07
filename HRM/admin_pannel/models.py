from django.db import models
from django.contrib.auth.models import User

DESIGNATION_CHOICES = (
    ("FE", "Frondend Developer"),
    ("BE", "Backend Developer"),
    ("FD", "Fullstack Developer"),
)
GENDER_CHOICES = (("male", "Male"), ("female", "Female"))


class UserLookUp(models.Model):
    class meta:
        db_table = "hrm_user_lookup"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    log_status = models.BooleanField(default=False)
    designation = models.CharField(choices=DESIGNATION_CHOICES)
    gender = models.CharField(choices=GENDER_CHOICES)
