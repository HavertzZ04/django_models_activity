# Generated by Django 5.0.7 on 2024-07-19 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_product_buy_price_alter_product_sell_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default=0, max_length=80),
            preserve_default=False,
        ),
    ]
