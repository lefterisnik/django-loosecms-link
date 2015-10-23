# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_link', '0002_auto_20150916_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='order',
        ),
    ]
