# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0010_profile_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='expiration_date',
            field=models.DateTimeField(null=True),
        ),
    ]
