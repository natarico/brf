# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamestats',
            name='health',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='gamestats',
            name='nuclear',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='gamestats',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gamestats',
            name='twinkies',
            field=models.IntegerField(default=0),
        ),
    ]
