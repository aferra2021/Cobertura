# Generated by Django 3.0.6 on 2020-06-01 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RecargasCubacel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranferenciaCubacel',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField()),
                ('SendValue', models.IntegerField()),
                ('accountNumber', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RecargasCubacel.Cliente')),
            ],
        ),
        migrations.DeleteModel(
            name='Tranferencia',
        ),
    ]
