# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0026_auto_20161209_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.FileField(upload_to='ewords/ewords/static/audio'),
        ),
    ]
