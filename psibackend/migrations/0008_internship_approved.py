# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0007_remove_internship_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
