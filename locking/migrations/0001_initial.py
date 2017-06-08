# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locked_object', models.CharField(unique=True, max_length=255, verbose_name='locked object')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', db_index=True)),
                ('max_age', models.PositiveIntegerField(default=3600, help_text='The age of a lock before it can be overwritten. 0 means indefinitely.', verbose_name='Maximum lock age')),
            ],
            options={
                'ordering': ['created_on'],
                'verbose_name': 'Lock',
                'verbose_name_plural': 'Locks',
            },
            bases=(models.Model,),
        ),
    ]
