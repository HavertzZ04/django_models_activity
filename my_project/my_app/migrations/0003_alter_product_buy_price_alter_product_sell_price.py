# Generated by Django 5.0.7 on 2024-07-19 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='buy_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='sell_price',
            field=models.IntegerField(),
        ),
    ]
