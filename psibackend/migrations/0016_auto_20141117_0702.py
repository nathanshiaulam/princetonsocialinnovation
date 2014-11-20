# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0015_auto_20141117_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='identifier',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'media/events/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='funnypicture',
            field=models.ImageField(null=True, upload_to=b'media/members/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'media/members/', blank=True),
            preserve_default=True,
        ),
    ]
