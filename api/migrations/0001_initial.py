# Generated by Django 4.1.4 on 2022-12-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=200)),
                ('vendor_number', models.IntegerField(default=0)),
                ('agreement_number', models.CharField(max_length=120)),
                ('contract_status', models.CharField(max_length=64)),
                ('contract_category', models.CharField(max_length=40)),
                ('contract_date', models.DateTimeField(verbose_name='contract_date')),
                ('contract_expiry', models.DateTimeField(verbose_name='contract_expiry')),
            ],
        ),
    ]