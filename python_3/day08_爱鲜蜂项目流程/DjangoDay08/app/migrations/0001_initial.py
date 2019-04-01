# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-06 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_title', models.CharField(max_length=100)),
                ('n_time', models.DateTimeField(auto_now=True)),
                ('n_content', models.TextField()),
            ],
        ),
    ]
