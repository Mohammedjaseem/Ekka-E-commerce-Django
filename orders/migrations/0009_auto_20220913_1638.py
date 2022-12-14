# Generated by Django 3.2.9 on 2022-09-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Ready to ship', 'Ready to ship'), ('On shipping', 'On shipping'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('return', 'return'), ('Refunded', 'Refunded')], default='Accepted', max_length=50),
        ),
    ]
