# Generated by Django 3.0.6 on 2020-06-01 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecargasCubacel', '0002_auto_20200531_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Apellidos',
            new_name='apellidos',
        ),
        migrations.AddField(
            model_name='cliente',
            name='correo',
            field=models.CharField(default=23, max_length=100),
            preserve_default=False,
        ),
    ]