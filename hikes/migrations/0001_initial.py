# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('date', models.DateField(default=datetime.date.today)),
                ('map_id', models.CharField(default=None, max_length=64)),
                ('map_container_id', models.CharField(default=None, max_length=64)),
            ],
        ),
    ]
