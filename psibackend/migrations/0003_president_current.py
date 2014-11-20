# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0002_remove_president_current'),
    ]

    operations = [
        migrations.AddField(
            model_name='president',
            name='current',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
