# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0022_member_creationdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='creationdate',
        ),
    ]
