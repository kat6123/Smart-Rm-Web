# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trash_manager', '0002_auto_20170615_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='dry_run',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='regex',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='task',
            name='remove_mode',
            field=models.CharField(choices=[('F', 'file'), ('D', 'directory'), ('R', 'recursive')], default='F', max_length=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('R', 'running'), ('C', 'completed'), ('W', 'waiting')], default='W', max_length=10),
        ),
        migrations.AlterField(
            model_name='trash',
            name='remove_mode',
            field=models.CharField(choices=[('F', 'file'), ('D', 'directory'), ('R', 'recursive')], default='F', max_length=10),
        ),
    ]
