# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-29 22:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20171129_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='goods_num',
            new_name='nums',
        ),
    ]
