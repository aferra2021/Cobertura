# Generated by Django 3.0.7 on 2020-08-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0020_transferenciaactual_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tranferenciageneral',
            name='Descripcion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='transferenciaactual',
            name='Descripcion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]