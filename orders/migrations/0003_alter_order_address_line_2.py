# Generated by Django 4.1 on 2022-08-27 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_orderproducts_orderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
