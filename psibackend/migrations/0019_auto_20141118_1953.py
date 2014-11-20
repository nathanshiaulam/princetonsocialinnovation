# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0018_auto_20141118_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='funnypicture',
            field=models.ImageField(null=True, upload_to=b'members/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'members/', blank=True),
            preserve_default=True,
        ),
    ]
