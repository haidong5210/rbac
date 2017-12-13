# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 02:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_auto_20171108_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rbac.Group', verbose_name='权限组'),
            preserve_default=False,
        ),
    ]
