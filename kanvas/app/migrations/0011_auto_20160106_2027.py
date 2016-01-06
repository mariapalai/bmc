# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20151221_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='canvas',
            name='links',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='canvas',
            name='products',
            field=models.TextField(blank=True),
        ),
    ]
