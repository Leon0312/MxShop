# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_goods_fav_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='shop_price',
            field=models.FloatField(default=0, verbose_name='售价'),
        ),
    ]
