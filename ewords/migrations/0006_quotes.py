# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ewords', '0005_mainquote_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('eng_text', models.TextField()),
                ('eng_author', models.CharField(max_length=200)),
                ('rus_text', models.TextField()),
                ('rus_author', models.CharField(max_length=200)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
