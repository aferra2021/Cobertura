# Generated by Django 3.0.7 on 2020-09-09 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0025_transferenciaactual_cant'),
    ]

    operations = [
        migrations.AddField(
            model_name='tranferenciageneral',
            name='TransferRef',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
