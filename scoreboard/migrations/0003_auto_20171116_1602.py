# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0002_auto_20171115_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='game_data',
            new_name='game_date',
        ),
    ]
