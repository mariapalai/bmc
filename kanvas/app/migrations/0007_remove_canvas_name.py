# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_canvas_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canvas',
            name='name',
        ),
    ]
