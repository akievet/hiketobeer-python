# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hikes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hike',
            name='image_file_name',
            field=models.CharField(default=None, max_length=64),
        ),
    ]
