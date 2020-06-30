# Generated by Django 3.0.6 on 2020-05-31 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('Apellidos', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tranferencia',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RecargasCubacel.Cliente')),
            ],
        ),
    ]