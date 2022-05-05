# Generated by Django 4.0.4 on 2022-05-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turiviusapi', '0008_remove_taxcalculator_taxed_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxcalculator',
            name='products',
            field=models.JSONField(null=True, verbose_name='products'),
        ),
        migrations.AlterField(
            model_name='taxcalculator',
            name='raw_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Brute Value'),
        ),
        migrations.AlterField(
            model_name='taxcalculator',
            name='total_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total Value'),
        ),
    ]
