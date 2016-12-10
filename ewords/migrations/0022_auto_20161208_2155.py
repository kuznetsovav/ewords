# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ewords', '0021_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='ewords/static/audio')),
                ('lyrics', tinymce.models.HTMLField()),
                ('link', models.CharField(max_length=200)),
                ('tag', models.CharField(max_length=200)),
                ('incognito', models.BooleanField()),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='incognito',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='incognito',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
