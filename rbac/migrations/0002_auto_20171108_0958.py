# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 01:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='权限组名称')),
            ],
        ),
        migrations.AlterModelOptions(
            name='permission',
            options={'verbose_name_plural': '权限表'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name_plural': '角色表'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': '用户表'},
        ),
        migrations.AddField(
            model_name='role',
            name='code',
            field=models.CharField(default=1, max_length=32, verbose_name='编码'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='rbac.Permission', verbose_name='具有的所有权限'),
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(blank=True, to='rbac.Role', verbose_name='具有的所有角色'),
        ),
        migrations.AddField(
            model_name='role',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Group', verbose_name='权限组'),
        ),
    ]
