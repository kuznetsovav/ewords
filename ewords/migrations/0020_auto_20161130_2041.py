# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0019_auto_20161127_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapuserquote',
            name='quote',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mapuserquote',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
