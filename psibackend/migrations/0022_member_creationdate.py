# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0021_delete_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='creationdate',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 21, 9, 49, 22, 856425), editable=False, blank=True),
            preserve_default=True,
        ),
    ]
