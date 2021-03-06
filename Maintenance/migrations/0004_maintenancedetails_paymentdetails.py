# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-20 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maintenance', '0003_registeredapartuser_unmatchedregistrations'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_id', models.CharField(max_length=50)),
                ('block_name', models.CharField(max_length=50)),
                ('flat_number', models.CharField(max_length=50)),
                ('maintenance_due', models.CharField(max_length=20)),
                ('maintenance_due_date', models.CharField(max_length=20)),
                ('month_year', models.CharField(max_length=10)),
                ('remaining_due', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('apartment_id', models.CharField(max_length=50)),
                ('block_name', models.CharField(max_length=50)),
                ('flat_number', models.CharField(max_length=50)),
                ('maintenance_due', models.CharField(max_length=20)),
                ('maintenance_due_date', models.CharField(max_length=20)),
                ('month_year', models.CharField(max_length=10)),
                ('paid_amount', models.CharField(max_length=20)),
                ('paid_date', models.CharField(max_length=20)),
                ('transaction_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]
