# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0029_auto_20161210_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='tag',
            field=models.CharField(default=datetime.datetime(2016, 12, 10, 14, 10, 40, 716107, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
