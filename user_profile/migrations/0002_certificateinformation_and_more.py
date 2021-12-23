# Generated by Django 4.0 on 2021-12-23 00:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateInformation',
            fields=[
                ('certificate_id', models.AutoField(primary_key=True, serialize=False)),
                ('certificate_number', models.CharField(max_length=50, null=True)),
                ('certificate_limitations_airborne_heater', models.BooleanField(default=True)),
                ('certificate_issue_date', models.DateField(default=datetime.date(2021, 12, 23))),
                ('certificate_rating', models.CharField(choices=[('student', 'Student Rating'), ('private', 'Private Rating'), ('commercial', 'Commercial Rating')], default='student', max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='pilotinformation',
            name='certificate_information',
            field=models.ForeignKey(default=99999, on_delete=django.db.models.deletion.CASCADE, to='user_profile.certificateinformation'),
            preserve_default=False,
        ),
    ]
