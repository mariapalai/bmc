# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151028_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canvas',
            name='relatedcompany',
        ),
        migrations.AddField(
            model_name='canvas',
            name='company',
            field=models.CharField(default='coka', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='canvas',
            name='logo',
            field=models.ImageField(default='documents/2015/10/28/cocacola.png', upload_to=b'documents/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
