# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadFile',
        ),
        migrations.AlterField(
            model_name='datavalue',
            name='value',
            field=models.IntegerField(verbose_name='Value'),
        ),
    ]
