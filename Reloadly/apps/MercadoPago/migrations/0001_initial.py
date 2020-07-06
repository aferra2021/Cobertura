# Generated by Django 3.0.7 on 2020-07-06 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteMercadoPago',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('area_Code', models.IntegerField()),
                ('number', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
                ('numberIdentifications', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('date_last_updated', models.DateTimeField(null=True)),
            ],
        ),
    ]
