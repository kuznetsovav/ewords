# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import tinymce.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0024_auto_20161209_0649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio',
            old_name='lyrics',
            new_name='lyrics_eng',
        ),
        migrations.AddField(
            model_name='audio',
            name='lyrics_rus',
            field=tinymce.models.HTMLField(default=datetime.datetime(2016, 12, 9, 4, 8, 43, 137303, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='ewords/static/images'),
        ),
    ]
