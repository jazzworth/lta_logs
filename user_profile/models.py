from django.db import models
from datetime import date


class PilotInformation(models.Model):
    pilot_id = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    company_name = models.CharField(max_length=254)
    street_number = models.CharField(max_length=16)
    street_name = models.CharField(max_length=64)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=12)
    email = models.EmailField(max_length=254, null=False)
    phone = models.CharField(max_length=16)
    certificate_information = models.ForeignKey('CertificateInformation', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()


class CertificateInformation(models.Model):
    STUDENT = 'student'
    PRIVATE = 'private'
    COMMERCIAL = 'commercial'
    RATING = [
        (STUDENT, ('Student Rating')),
        (PRIVATE, ('Private Rating')),
        (COMMERCIAL, ('Commercial Rating')),
    ]

    certificate_id = models.AutoField(primary_key=True, null=False)
    certificate_number = models.CharField(max_length=50, null=True)
    certificate_limitations_airborne_heater = models.BooleanField(default=True)
    certificate_issue_date = models.DateField(default=date.today())
    certificate_rating = models.CharField(max_length=32, choices=RATING, default=STUDENT)


    def __str__(self) -> str:
        return super().__str__()
