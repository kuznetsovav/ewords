# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0003_auto_20160424_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainquote',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
