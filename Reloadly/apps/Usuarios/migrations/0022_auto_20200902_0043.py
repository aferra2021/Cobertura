# Generated by Django 3.0.7 on 2020-09-02 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0021_auto_20200812_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='accountNumber',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='transferenciaactual',
            name='accountNumber',
            field=models.CharField(max_length=100),
        ),
    ]