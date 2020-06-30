# Generated by Django 3.0.6 on 2020-06-03 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RecargasCubacel', '0004_auto_20200601_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tranferenciacubacel',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
