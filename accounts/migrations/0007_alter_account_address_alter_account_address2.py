# Generated by Django 4.1 on 2022-08-24 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_account_address_account_address2_account_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='account',
            name='address2',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
