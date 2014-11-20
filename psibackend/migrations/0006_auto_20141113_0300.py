# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psibackend', '0005_president_current'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('year', models.CharField(max_length=150)),
                ('picture', models.ImageField(null=True, upload_to=b'media/', blank=True)),
                ('funnypicture', models.ImageField(null=True, upload_to=b'media/', blank=True)),
                ('position', models.CharField(max_length=150)),
                ('bio', models.TextField()),
                ('current', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='President',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.AddField(
            model_name='event',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'media/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'media/', blank=True),
            preserve_default=True,
        ),
    ]
