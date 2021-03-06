# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-03 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_page_is_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='pages.Page'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(),
        ),
    ]
