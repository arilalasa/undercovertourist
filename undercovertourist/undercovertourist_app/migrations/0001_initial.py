# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_purchasedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_phone', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('confirmation_code', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=100)),
            ],
        ),
    ]
