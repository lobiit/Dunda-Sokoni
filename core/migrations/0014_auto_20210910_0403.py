# Generated by Django 3.1.3 on 2021-09-10 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_courier_fcm_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='stripe_card_last4',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='stripe_customer_id',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='stripe_payment_method_id',
        ),
    ]
