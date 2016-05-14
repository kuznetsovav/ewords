# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0012_remove_quote_day_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='day_quote',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
