# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0020_subscriber'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]
