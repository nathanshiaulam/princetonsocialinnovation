# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0006_auto_20141113_0300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internship',
            name='picture',
        ),
    ]
