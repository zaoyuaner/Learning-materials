# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-21 08:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='a_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app3.UserModel'),
        ),
    ]
