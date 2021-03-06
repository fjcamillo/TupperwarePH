# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-30 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_onclickcart_cart_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onclickcart',
            name='cart_count',
        ),
        migrations.RemoveField(
            model_name='onclickcart',
            name='cart_summation',
        ),
        migrations.RemoveField(
            model_name='onclickcart',
            name='cart_tax',
        ),
        migrations.RemoveField(
            model_name='onclickcart',
            name='cart_title',
        ),
        migrations.RemoveField(
            model_name='onclickcart',
            name='cart_vat',
        ),
        migrations.AddField(
            model_name='onclickcart',
            name='product_cart_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='onclickcart',
            name='product_cart_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='onclickcart',
            name='product_cart_title',
            field=models.CharField(default='ProductName', max_length=150),
        ),
    ]
