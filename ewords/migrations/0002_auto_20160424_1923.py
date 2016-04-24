# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainquote',
            name='created_date',
            field=models.DateField(),
        ),
    ]
