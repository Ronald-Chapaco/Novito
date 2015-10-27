# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='acronimo',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='direccion',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='fax',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='fecha_fun',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nit',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='obj_actividad',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='telefono',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tipo',
            field=models.CharField(default=b'Otros', max_length=20, choices=[(b'Comercial', b'Comercial'), (b'Industrial', b'Industrial'), (b'Servicio', b'Servicio'), (b'Otros', b'Otros')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='titulo',
            field=models.CharField(default=b'Original', max_length=50),
        ),
    ]
