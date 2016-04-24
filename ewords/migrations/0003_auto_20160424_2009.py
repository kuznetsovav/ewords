# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0002_auto_20160424_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainquote',
            name='author',
        ),
        migrations.RemoveField(
            model_name='mainquote',
            name='published_date',
        ),
    ]
