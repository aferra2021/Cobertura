# Generated by Django 3.0.7 on 2020-07-06 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MercadoPago', '0001_initial'),
        ('Usuarios', '0010_auto_20200704_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='accountnumber',
            new_name='accountNumber',
        ),
        migrations.AddField(
            model_name='tranferenciageneral',
            name='clienteMercadoPago',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='MercadoPago.ClienteMercadoPago'),
            preserve_default=False,
        ),
    ]
