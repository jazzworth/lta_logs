# Generated by Django 4.0 on 2021-12-16 23:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='balloon',
            name='balloon_airworthiness_date',
            field=models.DateField(default=datetime.date(2021, 12, 16)),
        ),
        migrations.AddField(
            model_name='balloon',
            name='balloon_registration_expiration',
            field=models.DateField(default=datetime.date(2021, 12, 16)),
        ),
    ]
