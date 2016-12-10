# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0028_article_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='short_description',
            field=tinymce.models.HTMLField(max_length=500),
        ),
    ]
