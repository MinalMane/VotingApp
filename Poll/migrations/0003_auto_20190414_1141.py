# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-14 06:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0002_auto_20190414_0007'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice_text',
            new_name='Choice',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='choice',
        ),
    ]
