# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-29 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='onclickcart',
            name='cart_tax',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
