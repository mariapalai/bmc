# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_canvas_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canvas',
            name='activities',
            field=djrichtextfield.models.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='channels',
            field=djrichtextfield.models.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='cost',
            field=djrichtextfield.models.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='customer_segments',
            field=djrichtextfield.models.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='description',
            field=djrichtextfield.models.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='partners',
            field=djrichtextfield.models.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='relationships',
            field=djrichtextfield.models.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='resources',
            field=djrichtextfield.models.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='revenue',
            field=djrichtextfield.models.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='canvas',
            name='value_propositions',
            field=djrichtextfield.models.RichTextField(blank=True),
        ),
    ]
