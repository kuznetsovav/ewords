# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0027_auto_20161209_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='short_description',
            field=tinymce.models.HTMLField(default=datetime.datetime(2016, 12, 10, 11, 28, 18, 972333, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
