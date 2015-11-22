# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Canvas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=30)),
                ('createdby', models.CharField(max_length=20)),
                ('value_propositions', models.TextField(blank=True)),
                ('customer_segments', models.CharField(max_length=200)),
                ('partners', models.CharField(max_length=200)),
                ('relationships', models.CharField(max_length=200)),
                ('channels', models.CharField(max_length=200)),
                ('activities', models.CharField(max_length=200)),
                ('resources', models.CharField(max_length=200)),
                ('revenue', models.CharField(max_length=200)),
                ('cost', models.CharField(max_length=200)),
                ('originalauthor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('logo', models.FileField(upload_to=b'documents/%Y/%m/%d')),
            ],
        ),
    ]
