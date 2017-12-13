# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 03:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0007_auto_20171109_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='menu_gp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='xm', to='rbac.Permission', verbose_name='组内菜单'),
        ),
    ]
