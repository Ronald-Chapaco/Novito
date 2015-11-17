# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evento', '0005_auto_20151110_0450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rueda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=500)),
                ('fecha_creacion', models.DateField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('imagen', models.ImageField(default=b'images/calendario-default.png', upload_to=b'eventos')),
                ('lugar', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=50)),
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
                ('creador', models.ForeignKey(related_name='rudas_creados', to=settings.AUTH_USER_MODEL)),
                ('tipo', models.ManyToManyField(related_name='sectores', null=True, to='evento.TipoSector', blank=True)),
            ],
            options={
                'verbose_name': 'Rueda',
                'verbose_name_plural': 'Ruedas',
            },
        ),
    ]
