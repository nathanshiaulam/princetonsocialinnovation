# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0023_remove_member_creationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='croppedPicture',
            field=models.ImageField(null=True, upload_to=b'news/', blank=True),
            preserve_default=True,
        ),
    ]
