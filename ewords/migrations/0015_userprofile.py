# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ewords', '0014_auto_20160521_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('birthday', models.DateField(default=django.utils.timezone.now)),
                ('hobby', models.TextField(blank=True)),
                ('education', models.TextField(blank=True)),
                ('picture', models.ImageField(upload_to='profile_images', blank=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
