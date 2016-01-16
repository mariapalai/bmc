# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20160115_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canvas',
            name='logo',
            field=easy_thumbnails.fields.ThumbnailerImageField(default=b'/media/ntua-logo.gif', upload_to=b''),
        ),
    ]
