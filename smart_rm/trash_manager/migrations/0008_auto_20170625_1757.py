# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trash_manager', '0007_auto_20170623_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='paths',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='remove_mode',
            field=models.CharField(choices=[('F', 'file'), ('D', 'directory'), ('R', 'recursive')], default='R', max_length=10),
        ),
        migrations.AlterField(
            model_name='trash',
            name='remove_mode',
            field=models.CharField(choices=[('F', 'file'), ('D', 'directory'), ('R', 'recursive')], default='R', max_length=10),
        ),
    ]