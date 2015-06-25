# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0002_auto_20150611_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='Article.Category', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='projects',
            field=models.ManyToManyField(to='Article.Project', blank=True),
        ),
    ]
