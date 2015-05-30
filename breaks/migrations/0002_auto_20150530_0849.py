# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('breaks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='break',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='break',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 30, 8, 49, 16, 409032, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
