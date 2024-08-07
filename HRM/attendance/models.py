from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class userAttendance(models.Model):
    class Meta:
        db_table = "hrm_user_attendance"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date = models.DateField(null=False)
    log_in = models.DateTimeField(null=False)
    log_out = models.DateTimeField(null=False)
