# Generated by Django 4.0.4 on 2022-04-30 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turiviusapi', '0003_product_tax_taxcalculator_delete_icmscalculator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxcalculator',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turiviusapi.product'),
        ),
    ]
