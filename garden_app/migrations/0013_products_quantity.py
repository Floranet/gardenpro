# Generated by Django 5.1 on 2024-09-28 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden_app', '0012_rename_sell_details_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
