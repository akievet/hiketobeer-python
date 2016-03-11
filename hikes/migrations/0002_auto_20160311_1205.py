# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hikes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hikes',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='hikes',
            name='map_id',
            field=models.CharField(max_length=64, default=None),
        ),
        migrations.AddField(
            model_name='hikes',
            name='name',
            field=models.CharField(max_length=128, default=''),
        ),
    ]
