# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0015_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='day_quote',
            new_name='incognito',
        ),
    ]
