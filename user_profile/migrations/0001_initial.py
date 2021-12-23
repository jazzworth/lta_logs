# Generated by Django 4.0 on 2021-12-16 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PilotInformation',
            fields=[
                ('pilot_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=254)),
                ('street_number', models.CharField(max_length=16)),
                ('street_name', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=254)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16)),
            ],
        ),
    ]