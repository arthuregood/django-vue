# Generated by Django 4.0.4 on 2022-05-04 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turiviusapi', '0009_alter_taxcalculator_products_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxcalculator',
            name='tax_value',
            field=models.IntegerField(default=0, verbose_name='Tax Value'),
        ),
        migrations.AlterField(
            model_name='taxcalculator',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
