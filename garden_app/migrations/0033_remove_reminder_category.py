# Generated by Django 5.1.3 on 2025-01-19 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garden_app', '0032_reminder_task_status_reminder_task_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='category',
        ),
    ]
