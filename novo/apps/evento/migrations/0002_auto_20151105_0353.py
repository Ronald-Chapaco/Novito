# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='creador',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='invitados',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='localizacion',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='localidad',
            name='provincia',
        ),
        migrations.RemoveField(
            model_name='localizacion',
            name='localidad',
        ),
        migrations.RemoveField(
            model_name='provincia',
            name='pais',
        ),
        migrations.DeleteModel(
            name='Rubro',
        ),
        migrations.DeleteModel(
            name='Evento',
        ),
        migrations.DeleteModel(
            name='Localidad',
        ),
        migrations.DeleteModel(
            name='Localizacion',
        ),
        migrations.DeleteModel(
            name='Pais',
        ),
        migrations.DeleteModel(
            name='Provincia',
        ),
        migrations.DeleteModel(
            name='TipoEvento',
        ),
    ]
