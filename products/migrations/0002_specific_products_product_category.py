# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-26 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specific_products',
            name='product_category',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
