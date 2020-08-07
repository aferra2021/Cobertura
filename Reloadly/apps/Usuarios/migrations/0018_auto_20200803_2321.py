# Generated by Django 3.0.7 on 2020-08-04 03:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Usuarios', '0017_auto_20200803_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
