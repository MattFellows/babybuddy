# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Children',
                'ordering': ['last_name', 'first_name'],
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='DiaperChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('wet', models.BooleanField()),
                ('solid', models.BooleanField()),
                ('color', models.CharField(blank=True, choices=[('black', 'Black'), ('brown', 'Brown'), ('green', 'Green'), ('yellow', 'Yellow')], max_length=255)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diaper_change', to='core.Child')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('type', models.CharField(choices=[('breast milk', 'Breast milk'), ('formula', 'Formula')], max_length=255)),
                ('method', models.CharField(choices=[('bottle', 'Bottle'), ('left breast', 'Left breast'), ('right breast', 'Right breast')], max_length=255)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeding', to='core.Child')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'ordering': ['-start'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note', to='core.Child')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sleep', to='core.Child')),
            ],
            options={
                'verbose_name_plural': 'Sleep',
                'ordering': ['-start'],
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='TummyTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('milestone', models.CharField(blank=True, max_length=255)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tummy_time', to='core.Child')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'ordering': ['-start'],
            },
        ),
    ]