# Generated by Django 4.1.1 on 2022-10-16 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_deals_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='already_saled',
            field=models.IntegerField(default=23),
        ),
    ]