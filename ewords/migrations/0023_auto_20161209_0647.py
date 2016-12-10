# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0022_auto_20161208_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.FileField(upload_to='static/audio'),
        ),
    ]
