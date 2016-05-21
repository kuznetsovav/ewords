# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0013_quote_day_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainquote',
            name='author',
        ),
        migrations.AddField(
            model_name='quote',
            name='category',
            field=models.CharField(default='Happiness', max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MainQuote',
        ),
    ]
