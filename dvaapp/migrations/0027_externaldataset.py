# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0026_remove_indexentries_framelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algorithm', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('count_images', models.IntegerField()),
                ('count_entries', models.IntegerField()),
                ('cached_image_count', models.IntegerField()),
                ('index_downloaded', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
    ]