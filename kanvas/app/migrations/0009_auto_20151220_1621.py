# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_canvas_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canvas',
            name='activities',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='channels',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='cost',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='customer_segments',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='description',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='partners',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='relationships',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='resources',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='revenue',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='value_propositions',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
