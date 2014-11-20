# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0017_auto_20141117_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(default=None, max_length=150, blank=True)),
                ('subject', models.CharField(default=None, max_length=150, blank=True)),
                ('message', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'events/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'news/', blank=True),
            preserve_default=True,
        ),
    ]
