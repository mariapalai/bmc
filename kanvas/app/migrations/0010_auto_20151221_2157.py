# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20151220_1621'),
    ]

    operations = [
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
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='logo',
            field=models.ImageField(default=b'/media/default-logo.png', upload_to=b'documents/%Y/%m/%d'),
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
        migrations.AlterField(
            model_name='canvas',
            name='value_propositions',
            field=models.TextField(blank=True),
        ),
    ]
