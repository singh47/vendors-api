# Generated by Django 4.1.4 on 2022-12-12 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendors',
            name='contract_date',
            field=models.DateField(verbose_name='contract_date'),
        ),
        migrations.AlterField(
            model_name='vendors',
            name='contract_expiry',
            field=models.DateField(verbose_name='contract_expiry'),
        ),
    ]