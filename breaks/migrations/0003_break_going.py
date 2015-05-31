# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('breaks', '0002_auto_20150530_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='break',
            name='going',
            field=models.ManyToManyField(related_name='users_going', to=settings.AUTH_USER_MODEL),
        ),
    ]
