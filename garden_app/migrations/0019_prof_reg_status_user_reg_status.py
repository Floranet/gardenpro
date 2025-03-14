# Generated by Django 5.1 on 2024-10-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden_app', '0018_remove_prof_reg_img_remove_user_reg_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof_reg',
            name='status',
            field=models.CharField(choices=[('applied', 'Applied'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='applied', max_length=20),
        ),
        migrations.AddField(
            model_name='user_reg',
            name='status',
            field=models.CharField(choices=[('applied', 'Applied'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='applied', max_length=20),
        ),
    ]
