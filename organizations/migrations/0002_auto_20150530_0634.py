# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import durationfield.db.models.fields.duration


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Break',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=300)),
                ('duration', durationfield.db.models.fields.duration.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='org_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='org_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='org_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='office',
            name='organization',
            field=models.ForeignKey(to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='break',
            name='office',
            field=models.ForeignKey(to='organizations.Office'),
        ),
    ]
