# Generated by Django 4.1 on 2022-08-24 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_account_email2'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone_number2',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
