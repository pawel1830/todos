# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-16 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_tasks_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='details',
            field=models.TextField(null=True),
        ),
    ]