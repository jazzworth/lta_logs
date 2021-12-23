from django.db import models

from datetime import datetime, date


class Balloon(models.Model):
    balloon_id = models.AutoField(primary_key=True, null=False)
    balloon_n_number = models.CharField(max_length=16)
    balloon_make = models.CharField(max_length=50)
    balloon_size = models.CharField(max_length=50)
    balloon_model = models.CharField(max_length=50)
    balloon_name = models.CharField(max_length=50)
    balloon_airworthiness_date = models.DateField(default=date.today())
    balloon_registration_expiration = models.DateField(default=date.today())

    def __str__(self) -> str:
        return super().__str__()