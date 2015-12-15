# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20151214_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='canvas',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
