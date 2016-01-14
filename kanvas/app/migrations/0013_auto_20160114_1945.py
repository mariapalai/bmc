# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_canvas_opinion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canvas',
            name='opinion',
        ),
        migrations.AlterField(
            model_name='canvas',
            name='logo',
            field=models.ImageField(default=b'/media/ntua-logo.gif', upload_to=b'documents/%Y/%m/%d'),
        ),
    ]
