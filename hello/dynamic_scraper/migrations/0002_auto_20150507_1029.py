# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scraper',
            name='pagination_crawelerrule_xpath',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='scraper',
            name='pagination_type',
            field=models.CharField(default=b'N', max_length=1, choices=[(b'N', b'NONE'), (b'R', b'RANGE_FUNCT'), (b'F', b'FREE_LIST'), (b'C', b'CRAWLER_XPATH_ALLOW')]),
        ),
    ]
