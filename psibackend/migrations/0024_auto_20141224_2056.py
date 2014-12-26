# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0023_remove_member_creationdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='identifier',
        ),
        migrations.RemoveField(
            model_name='event',
            name='white',
        ),
    ]
