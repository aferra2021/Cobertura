# Generated by Django 3.0.7 on 2020-07-06 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MercadoPago', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientemercadopago',
            name='date_last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
