# Generated by Django 5.1 on 2024-11-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden_app', '0024_alter_products_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
