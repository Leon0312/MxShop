# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-29 22:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0003_auto_20171129_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userleavingmessage',
            old_name='msg_type',
            new_name='message_type',
        ),
    ]
