# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0010_quote_day_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='image_link',
            field=models.CharField(max_length=200, default=1),
            preserve_default=False,
        ),
    ]
