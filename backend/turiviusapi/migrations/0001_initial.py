# Generated by Django 4.0.4 on 2022-04-30 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IcmsCalculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TimeField(default=datetime.date.today, verbose_name='Date')),
                ('base_value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Base Value')),
                ('icms', models.IntegerField(verbose_name='ICMS')),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Total Value')),
            ],
        ),
    ]