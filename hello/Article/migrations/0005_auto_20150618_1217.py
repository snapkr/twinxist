# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0004_auto_20150611_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='article',
            field=models.ForeignKey(related_name='favorites', to='Article.Article'),
        ),
    ]
