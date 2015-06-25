# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_auto_20150611_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='post',
            new_name='article',
        ),
    ]
