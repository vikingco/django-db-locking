# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locking', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel('Lock', 'NonBlockingLock'),
        migrations.AlterModelOptions(
            name='nonblockinglock',
            options={'ordering': ['created_on'], 'verbose_name': 'NonBlockingLock', 'verbose_name_plural': 'NonBlockingLocks'},
        ),
    ]
