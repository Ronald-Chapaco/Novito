# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default=b'Nombre', max_length=30)),
                ('descripcion', models.TextField(max_length=300)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('fecha_creacion', models.DateField()),
                ('estado', models.CharField(default=b'noleido', max_length=30)),
                ('imagen', models.ImageField(default=b'images/calendario-default.png', upload_to=b'eventos')),
                ('creador', models.ForeignKey(related_name='eventos_creados', to=settings.AUTH_USER_MODEL)),
                ('invitados', models.ManyToManyField(related_name='eventos_invitado', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Localidades',
            },
        ),
        migrations.CreateModel(
            name='Localizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('barrio', models.CharField(max_length=20)),
                ('calle', models.CharField(max_length=20)),
                ('numero', models.IntegerField()),
                ('numero_local', models.IntegerField()),
                ('localidad', models.ForeignKey(to='evento.Localidad')),
            ],
            options={
                'verbose_name_plural': 'Localizaciones',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('pais', models.ForeignKey(to='evento.Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='localidad',
            name='provincia',
            field=models.ForeignKey(to='evento.Provincia'),
        ),
        migrations.AddField(
            model_name='evento',
            name='localizacion',
            field=models.ForeignKey(to='evento.Localizacion'),
        ),
        migrations.AddField(
            model_name='evento',
            name='tipo',
            field=models.ForeignKey(default=b'', blank=True, to='evento.TipoEvento', null=True),
        ),
    ]
