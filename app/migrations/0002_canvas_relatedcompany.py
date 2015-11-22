# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='canvas',
            name='relatedcompany',
            field=models.OneToOneField(default=None, to='app.Company'),
            preserve_default=False,
        ),
    ]
