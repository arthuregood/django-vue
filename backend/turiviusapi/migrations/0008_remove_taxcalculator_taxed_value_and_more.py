# Generated by Django 4.0.4 on 2022-05-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turiviusapi', '0007_alter_product_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxcalculator',
            name='taxed_value',
        ),
        migrations.RemoveField(
            model_name='taxcalculator',
            name='user',
        ),
        migrations.RemoveField(
            model_name='taxcalculator',
            name='value',
        ),
        migrations.AddField(
            model_name='taxcalculator',
            name='raw_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Brute Value'),
        ),
        migrations.AddField(
            model_name='taxcalculator',
            name='total_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Total Value'),
        ),
    ]
