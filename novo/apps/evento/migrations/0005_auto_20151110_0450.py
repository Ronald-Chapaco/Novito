# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0004_auto_20151110_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rueda',
            name='creador',
        ),
        migrations.RemoveField(
            model_name='rueda',
            name='tipo',
        ),
        migrations.DeleteModel(
            name='Rueda',
        ),
    ]
