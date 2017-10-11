# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 18:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health', models.IntegerField()),
                ('points', models.IntegerField()),
                ('twinkies', models.IntegerField()),
                ('nuclear', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='currentStats', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]