# Generated by Django 5.1.3 on 2025-01-19 09:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden_app', '0036_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
