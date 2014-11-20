# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0008_internship_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internship',
            name='name_of_internship',
        ),
        migrations.AddField(
            model_name='internship',
            name='email',
            field=models.EmailField(default=None, max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='internship',
            name='intern_role',
            field=models.CharField(default=None, max_length=150, blank=True),
            preserve_default=True,
        ),
    ]
