# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trash_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='paths',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trash',
            name='location',
            field=models.CharField(default='/home/katya/.local/share/trash', max_length=30),
        ),
    ]
