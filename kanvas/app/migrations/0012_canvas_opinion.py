# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20160106_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='canvas',
            name='opinion',
            field=models.IntegerField(default=0),
        ),
    ]
