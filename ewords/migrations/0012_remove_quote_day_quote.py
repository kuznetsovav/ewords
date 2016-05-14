# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0011_quote_image_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='day_quote',
        ),
    ]
