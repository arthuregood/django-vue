# Generated by Django 4.0.4 on 2022-04-30 17:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turiviusapi', '0002_icmscalculator_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=20)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Value')),
                ('taxed_value', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Taxed Value')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(default='', max_length=20)),
                ('value', models.IntegerField(default=0, verbose_name='Value')),
            ],
        ),
        migrations.CreateModel(
            name='TaxCalculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TimeField(default=datetime.date.today, verbose_name='Date')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Value')),
                ('taxed_value', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Taxed Value')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='IcmsCalculator',
        ),
        migrations.AddField(
            model_name='product',
            name='tax',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turiviusapi.tax'),
        ),
    ]
