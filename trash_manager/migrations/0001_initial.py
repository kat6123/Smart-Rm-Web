# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('path_in_trash', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('C', 'completed'), ('W', 'waiting')], default='W', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('location', models.FilePathField(default='/', path='/')),
                ('remove_mode', models.CharField(choices=[('F', 'file'), ('D', 'directory'), ('R', 'recursive')], default='F', max_length=1)),
                ('dry_run', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='trash',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trash_manager.Trash'),
        ),
        migrations.AddField(
            model_name='info',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trash_manager.Task'),
        ),
    ]
