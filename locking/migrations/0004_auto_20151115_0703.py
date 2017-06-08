# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('locking', '0003_optimize_queries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nonblockinglock',
            name='id',
        ),
        migrations.AddField(
            model_name='nonblockinglock',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
    ]
