# Generated by Django 3.0.7 on 2020-08-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0019_auto_20200812_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='transferenciaactual',
            name='Descripcion',
            field=models.CharField(default=23, max_length=200),
            preserve_default=False,
        ),
    ]