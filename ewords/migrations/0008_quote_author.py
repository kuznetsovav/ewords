# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ewords', '0007_auto_20160430_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
