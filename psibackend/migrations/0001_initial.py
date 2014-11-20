# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('date', models.DateTimeField(verbose_name=b'time of event')),
                ('tentative', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_of_internship', models.CharField(max_length=150)),
                ('employer', models.CharField(max_length=150)),
                ('picture', models.ImageField(null=True, upload_to=b'media/', blank=True)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('picture', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('date', models.DateField(verbose_name=b'date posted')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('year', models.CharField(max_length=150)),
                ('picture', models.ImageField(null=True, upload_to=b'media/', blank=True)),
                ('bio', models.TextField()),
                ('current', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('leaders', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
