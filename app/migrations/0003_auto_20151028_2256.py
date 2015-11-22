# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_canvas_relatedcompany'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canvas',
            name='createdby',
        ),
        migrations.AlterField(
            model_name='canvas',
            name='activities',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='channels',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='cost',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='customer_segments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='partners',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='relationships',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='resources',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='revenue',
            field=models.TextField(blank=True),
        ),
    ]
