# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0014_auto_20141117_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'media/news/', blank=True),
            preserve_default=True,
        ),
    ]
