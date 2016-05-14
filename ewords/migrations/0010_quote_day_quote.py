# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0009_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='day_quote',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
