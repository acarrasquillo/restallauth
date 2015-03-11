# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authdemo', '0002_auto_20150307_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 3, 7, 4, 45, 31, 334610, tzinfo=utc), unique=True, max_length=255, verbose_name=b'email address'),
            preserve_default=False,
        ),
    ]
