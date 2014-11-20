# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0016_auto_20141117_0702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='tentative',
            new_name='white',
        ),
    ]
